import os
import platform
import subprocess
import trafilatura
import jieba
from gtts import gTTS
from langdetect import detect
from googletrans import Translator
from summa.summarizer import summarize


class TextoAVoz:
    """
    Objeto que gestiona la conversión de texto a voz a partir de diferentes fuentes:
    texto fijo, entrada por teclado, archivos locales y artículos web.
    """

    def __init__(self):
        self.texto = "" #Atributo donde se guarda el texto a leer
    #Método texto fijo
    def leer_texto_fijo(self):
        self.texto = "Hola, esto es un texto fijo de prueba." 
        

    #Método texto entrada por teclado
    def leer_input(self):
        self.texto = input("De Texto a Voz, introduce el texto: ") 
       

    #Método texto archivos locales
    def leer_archivo(self, ruta):
        try:
           with open(ruta, "r", encoding="utf-8") as archivo:
               self.texto = archivo.read()              
        except FileNotFoundError:
            print("archivo no encontrado.")

    #Método texto artículos web
    def leer_url(self, url):
        try:
            downloaded = trafilatura.fetch_url(url)
            if downloaded:
                self.texto = trafilatura.extract(downloaded, include_comments = False)
            else:    
                self.texto = "No se pudo descargar el contenido"
        except Exception as e:
            print(f"Error al procesar la URL: {e}")

    #Método texto pasado a audio
    def reproducir(self):
        try:
           print("\n🎙️ INICIANDO CONVERSIÓN DE TEXTO A VOZ...")
           idioma_detectado = detect(self.texto)
           print(f"🌍 Idioma detectado: {idioma_detectado.upper()}")
           self.audio = gTTS(text=self.texto, lang=idioma_detectado)
           self.audio.save("audio.mp3")
           print("✅ Audio generado como 'audio.mp3'. Reproduciendo ahora...\n")

           print("🎯 Intentando reproducir el audio...")
           sistema = platform.system()
           print(f"🖥️ Sistema operativo detectado: {sistema}")
           if sistema == "Windows":
               os.startfile("audio.mp3")
           elif sistema == "Darwin":  # macOS
               subprocess.call(["afplay", "audio.mp3"])
           elif sistema == "Linux":
            subprocess.call(["xdg-open", "audio.mp3"])
           else:
            print("❌ Reproducción automática no soportada en este sistema.") #No es ninguno de los sistemas soportado
        except Exception as e:
            print(f"❌ Error al generar o reproducir el audio: {e}")

    #Método para resumir el texto >= 100 palabras
    def resumir_texto(self, min_palabras=100, num_oraciones=5):
        idioma_actual = detect(self.texto)#Si el idioma es chino, segmentamos con jieba

        if idioma_actual.startswith("zh"):
            print("🔍 Segmentando texto en chino con jieba...")
            palabras_chinas = list(jieba.cut(self.texto))
            texto_segmentado = " ".join(palabras_chinas)
        else:
             texto_segmentado = self.texto
        
        if len(texto_segmentado.split()) < min_palabras:    #Ya podemos comprobar la cantidad de palabras correctamente
            print(f"\n⚠️ El texto tiene menos de {min_palabras} palabras. No se puede resumir.")
            return

        print(f"\n🧠 Generando resumen...")
        resumen = summarize(self.texto, split = True)
        if resumen:
            resumen_texto = " ".join(resumen[:num_oraciones])
            self.texto = resumen_texto
            idioma_actual = detect(self.texto).upper()
            print(f"\n🔽🔽🔽 RESUMEN EN {idioma_actual} 🔽🔽🔽\n" + "-"*30)
            print(self.texto)
            return idioma_actual

   

    #Método para traducir el texto a otro idioma
    def traducir_texto(self, idioma_destino="en"):
        idioma_detectado = detect(self.texto)
        print(f"\n🌐 Traduciendo del idioma {idioma_detectado.upper()} a {idioma_destino.upper()}...")

        try:
            traductor = Translator()
            traduccion = traductor.translate(self.texto, src=idioma_detectado, dest=idioma_destino)
            self.texto = traduccion.text  # Sobrescribimos el texto con el traducido
            print("✅ Traducción completada.")  
            return idioma_detectado          
        except Exception as e:
            print(f"❌ Error al traducir el texto: {e}")
       
    #Método para contar palabras para determinar si hacer o no el resumen.
    def contar_palabras(self):
        idioma = detect(self.texto)
        if idioma.startswith("zh"):
            palabras = list(jieba.cut(self.texto))
            return len(palabras)
        else:
            return len(self.texto.split())
        


#CONDICIONAL PRINCIPAL PARA SELECCIONAR LA FUENTE DEL TEXTO.
if __name__ == "__main__":
    while True:
        texto_a_voz = TextoAVoz()
        
        print("Selecciona cómo quieres ingresar el texto:")
        print("1. Texto fijo")
        print("2. Introducir texto manualmente")
        print("3. Leer desde archivo")
        print("4. Leer desde URL")
        print("5. Salir del programa")

        opcion = input("Introduce una opción (1-5): ")

        if opcion == "1":
            texto_a_voz.leer_texto_fijo()
        elif opcion == "2":
            texto_a_voz.leer_input()
        elif opcion == "3":
            ruta = input("Introduce la ruta del archivo: ").strip('"')
            texto_a_voz.leer_archivo(ruta)
        elif opcion == "4":
            url = input("Introduce la URL del artículo: ")
            texto_a_voz.leer_url(url)
        elif opcion == "5":
            print("👋 Programa finalizado desde el menú principal. ¡Hasta pronto!")
            exit()
        else:
            print("Opción no válida.")
#Finalmente se reproduce (texto original o resumido)
        texto_a_voz.reproducir()

# ═════════════════════════════════════════════════════════════════════
#  OPCIONES SOBRE EL TEXTO CARGADO (resumen, traducción, volver, salir)
# ═════════════════════════════════════════════════════════════════════
        if texto_a_voz.texto:
            while True:
                print("\n🛠️ ¿Qué quieres hacer con el texto?")
                print("1. Escuchar resumen (si es largo)")
                print("2. Traducir a otro idioma")
                print("3. Volver al menú principal")
                print("4. Salir del programa")
                opcion_extra = input("Selecciona una opción (1-4): ")

# ═════════════════════════════════════
#  OPCIÓN 1 - Hacer resumen del texto
# ═════════════════════════════════════

                if opcion_extra == "1":
                    if texto_a_voz.contar_palabras() >= 100:
                        texto_a_voz.resumir_texto() 
                        texto_a_voz.reproducir()
                    else:
                        print("⚠️ El texto es muy corto para hacer un resumen.")

# ═══════════════════════════════════
#  OPCIÓN 2 - Traducir a otro idioma
# ═══════════════════════════════════

                elif opcion_extra == "2":
                    idiomas_permitidos = ["es", "en", "fr", "it", "de", "tr", "zh-cn"]
                    print("Idiomas disponibles:")
                    print(" es (español), en (inglés), fr (francés), it (italiano), de (alemán)")
                    print(" tr (turco), zh-cn (chino simplificado)")

                    idioma_destino = input("Introduce el código del idioma (o escribe 'x' para cancelar): ").lower()
                    if idioma_destino == "zh":
                         idioma_destino = "zh-cn"
                    
                    while idioma_destino not in idiomas_permitidos:
                        if idioma_destino == "x":
                            print("❌ Traducción cancelada.")
                            break
                        print("Código de idioma no válido. Intenta de nuevo.")
                        idioma_destino = input("Introduce el código del idioma: ").lower()

                    if idioma_destino in idiomas_permitidos:
                        texto_a_voz.traducir_texto(idioma_destino)
                        print(f"\n--- TEXTO TRADUCIDO ({idioma_destino.upper()}) ---\n")
                        print(texto_a_voz.texto)
                        texto_a_voz.reproducir()

# ═════════════════════════════════════
#  OPCIÓN 3 - Volver al menú principal
# ═════════════════════════════════════

                elif opcion_extra == "3":
                    break  # 🔁 Volver al menú principal
                elif opcion_extra == "4":
                    print("👋 Programa finalizado. ¡Hasta la próxima!")
                    exit()

# ══════════════════
#  Opción no válida
# ══════════════════

                else:
                    print("❌ Opción no válida.")








# -------------------------------------------------------------------------------------
# Descripción del programa:
# Este script permite ingresar texto desde diferentes fuentes (fijo, manual, archivo o URL),
# detecta su idioma automáticamente, da la opción de traducirlo a varios idiomas soportados
# (es, en, fr, it, de, tr, zh-cn), puede generar un resumen si el texto tiene más de 100 palabras,
# y convierte el texto final (original, resumido o traducido) en audio utilizando gTTS.
# -------------------------------------------------------------------------------------




"""
---------------------------------------------------------------
Este script permite convertir texto a voz desde distintas fuentes:
- Texto fijo
- Entrada manual
- Archivos locales
- Artículos extraídos desde una URL

Funcionalidades adicionales:
- Resume automáticamente textos largos (más de 100 palabras)
- Traduce el texto a diferentes idiomas (es, en, fr, it, de, tr, zh-cn)
- Reproduce el texto con voz usando gTTS

El flujo se adapta según las decisiones del usuario:
- Puede elegir si quiere un resumen del texto.
- Puede traducir el contenido antes o después del resumen.
- Ofrece una experiencia fluida con mensajes claros y voz generada.

Autor: José Cabello Romero
Fecha: 13/07/2025
---------------------------------------------------------------
"""


