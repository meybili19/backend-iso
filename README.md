---

### 📄 README.md

# 🌐 ISO/IEC 29100 Case Study App

Este proyecto es una aplicación web interactiva que permite generar, resolver y comparar casos de estudio relacionados con la norma **ISO/IEC 29100 (Privacidad y Protección de Datos)** usando inteligencia artificial (Gemini).  
Incluye un backend en **FastAPI (Python)** y un frontend en **Next.js (React)**.

---

## 📦 Estructura del proyecto

```

/backend   → API FastAPI con integración a Google Gemini
/frontend  → Interfaz web Next.js con Tailwind CSS

````

---

## 🚀 Requisitos previos

Asegúrate de tener instalado:
- [Node.js](https://nodejs.org) (v18 o superior)
- [Python](https://www.python.org) (v3.8 o superior)
- [Git](https://git-scm.com)
- Una API Key válida de **Google Gemini**

---

## 🛠 Instalación y ejecución

### 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/tu-repo.git
cd tu-repo
````

---

### 2️⃣ Backend (FastAPI)

```bash
cd backend
python -m venv venv
# Activar entorno virtual:
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

pip install -r requirements.txt
```

🔑 Configurar tu API Key Gemini:

* Opción directa (solo pruebas):

  * Edita `main.py` y escribe la clave directamente en `genai.configure(api_key="AQUI_TU_API_KEY")`.
* O mejor:

  * Usa variable de entorno:

    ```bash
    set GOOGLE_API_KEY=AQUI_TU_API_KEY   # Windows
    export GOOGLE_API_KEY=AQUI_TU_API_KEY # Mac/Linux
    ```

Luego, levanta el servidor:

```bash
uvicorn main:app --reload
```

El backend quedará disponible en:

```
http://localhost:8000
```

---

### 3️⃣ Frontend (Next.js)

```bash
cd frontend
npm install
npm run dev
```

El frontend quedará disponible en:

```
http://localhost:3000
```

---

## ⚙ Funcionalidades principales

✅ Generar casos de estudio ISO/IEC 29100 usando IA
✅ Permitir que el usuario ingrese su solución manual
✅ Obtener solución automática de la IA (Gemini)
✅ Comparar ambas soluciones, mostrando coincidencias y porcentaje
✅ Interfaz elegante y fácil de usar con Tailwind CSS
✅ Renderizado enriquecido de resultados usando Markdown

---

## 📂 Archivos ignorados (`.gitignore`)

El proyecto ya incluye `.gitignore` para evitar subir:

* `node_modules/`
* `.next/`
* `venv/`
* `.env` y claves sensibles
* Archivos temporales y logs

---

## 📜 Licencia

Este proyecto es solo para fines educativos y demostrativos.
Por favor, no uses las claves API compartidas para producción ni sobrepasar los límites gratuitos de Google Gemini.

---

````

---
