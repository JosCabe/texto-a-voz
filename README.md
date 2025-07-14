<!-- 1. Banner decorativo centrado -->
<p align="center">
  <img src="https://github.com/JosCabe/texto-a-voz/blob/main/banner.png?raw=true" width="800"/>
</p>

<!-- 2. Badges y título -->
<p align="center">
  <img src="https://img.shields.io/badge/Python-3.7%2B-blue?style=flat&logo=python" alt="Python Version">
  <img src="https://img.shields.io/github/license/JosCabe/texto-a-voz" alt="License">
</p>

<h1 align="center">🧠 Texto a Voz - Conversor Inteligente Multilenguaje</h1>

<!-- 3. Descripción corta -->
<p align="center">
  Convierte texto en voz, detecta idioma automáticamente, traduce, resume y reproduce en audio. Todo en un solo script.
</p>

<!-- 4. Estado del proyecto -->
<p align="center">
  <img src="https://img.shields.io/badge/Status-Activo-brightgreen" alt="Estado">
  <img src="https://img.shields.io/badge/Colaboraciones-Bienvenidas-blueviolet" alt="Colaboraciones">
</p>

---

<!-- 5. Descripción completa -->
Este proyecto permite convertir texto en voz a partir de diferentes fuentes. Además, puede detectar automáticamente el idioma, traducir el texto a varios idiomas disponibles, generar un resumen (si el texto es largo, concretamente mayor a 99 palabras) y reproducirlo en voz alta usando Google Text-to-Speech (`gTTS`).

---

## 🚀 Características

- ✅ Soporta múltiples fuentes de texto:
  - Texto fijo de prueba
  - Entrada manual del usuario
  - Archivos `.txt` locales
  - Artículos web (URLs)

- 🌍 Detecta automáticamente el idioma del texto.
- 🔁 Traduce el texto a varios idiomas soportados:
  - Español (`es`)
  - Inglés (`en`)
  - Francés (`fr`)
  - Italiano (`it`)
  - Alemán (`de`)
  - Turco (`tr`)
  - Chino simplificado (`zh-cn` o `cn`)

- 🧠 Si el texto tiene más de 100 palabras, puede generar un resumen automático con 5 oraciones clave.
- 🔊 Convierte el texto final en audio (`.mp3`) y lo reproduce automáticamente.

---

## 🛠️ Tecnologías y Librerías Usadas

- **Python 3.7+**
- `gTTS` – Google Text-to-Speech
- `langdetect` – Para detectar el idioma original
- `googletrans==4.0.0-rc1` – Para traducir el texto
- `summa` – Para generar resúmenes multilingües.
- `filatura`  – Para extraer textos de páginas web
- `jieba`  – Para segmentar textos en Chino.

---

## ▶️ Cómo usarlo

1. Asegúrate de tener Python 3 instalado.
2. Descarga este repositorio y ubica tu consola en la carpeta del proyecto.
3. Instala las dependencias ejecutando:

   ```bash
   pip install -r requirements.txt

   ```




## 👨‍💻 Autor

Proyecto creado por José Cabello Romero como ejercicio práctico de programación con Python.  
¡Libre de usar, modificar y mejorar!

---

## 🎯 Objetivo del Proyecto

Este proyecto nació como un reto personal para integrar diferentes librerías de Python en una aplicación funcional y útil.  
La idea es que cualquier usuario, sin conocimientos técnicos, pueda introducir texto, traducirlo y escucharlo fácilmente.

## 🔮 Posibles mejoras futuras

- Añadir una interfaz gráfica con Tkinter o PyQt.
- Permitir guardar múltiples audios generados.
- Integrar APIs externas para voces más naturales.
- Exportar resúmenes a PDF o TXT automáticamente.

---

## 📄 Licencia

Este proyecto está bajo la licencia MIT.  
Puedes usarlo libremente para fines personales o educativos.


