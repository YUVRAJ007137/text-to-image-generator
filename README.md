# Text-to-Image Generator using Stable Diffusion

## 📌 Project Overview
This is a **Text-to-Image Generator** web application built using **PHP (frontend)** and **Flask (backend)**, leveraging **Stable Diffusion** to generate images from textual prompts. The backend processes text inputs using a locally hosted **Stable Diffusion model** and returns generated images.

## 🚀 Features
- Enter text prompts to generate high-quality AI images
- Responsive and clean **Bootstrap-based UI**
- **AJAX integration** for smooth request handling
- **Flask API backend** for handling image generation
- Images are temporarily stored and displayed on the frontend

## 🛠️ Tech Stack
### Frontend:
- **HTML, CSS, JavaScript** (Bootstrap for styling)
- **AJAX** for sending requests to the backend

### Backend:
- **Flask (Python)**
- **Stable Diffusion (Hugging Face Diffusers)**
- **Torch & Transformers**

## 📂 Project Structure
```
📂 project-root/
│-- 📂 static/             # Static assets (CSS, JS, Images)
│-- 📂 templates/          # HTML Templates
│-- 📂 generated_images/   # Stores generated images temporarily
│-- 📄 app.py              # Flask backend
│-- 📄 requirements.txt    # Dependencies
│-- 📄 index.php           # PHP frontend
│-- 📄 README.md           # Project Documentation
```

## 🔧 Setup & Installation
### 1️⃣ Prerequisites
- **Python 3.8+**
- **PHP & XAMPP** (for local hosting of frontend)
- **Pip & Virtual Environment**
- **GPU (recommended) for faster image generation**

### 2️⃣ Install Dependencies
Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows
```
Install required Python libraries:
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Flask Server
```bash
python app.py
```
Server will start at: **http://127.0.0.1:5000/**

### 4️⃣ Run the Frontend (PHP)
1. Move frontend files to `htdocs` inside **XAMPP** folder.
2. Start **Apache server** via XAMPP.
3. Open in browser:
   ```
   http://localhost/index.php
   ```

## 🔗 API Endpoints
### `POST /generate`
**Request:**
```json
{
  "prompt": "A futuristic city at night"
}
```
**Response:**
```json
{
  "image_url": "/generated_images/output.png"
}
```

## 🎯 Future Improvements
- ✅ **Store generated images in a database** (e.g., Oracle 10g, MySQL)
- ✅ **User authentication & history tracking**
- ✅ **Enhance model performance & image quality**

## 💡 Contributing
Feel free to **fork** this repo, submit issues, and contribute to making it better!

---
**Developed with ❤️ by Yuvraj Chaudhari**

