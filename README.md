# 🧑‍💻 Abhishek's Personal Portfolio

A personal portfolio website built with **Django** — showcasing my projects, skills, and experience.

---

## 🌐 Live Demo

> 🚀 [View Portfolio](https://your-railway-url.up.railway.app) ← *(Replace with your Railway URL)*

---

## 🛠️ Tech Stack

- **Backend:** Python, Django
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite (default)
- **Deployment:** Railway

---

## ✨ Features

- Dynamic portfolio content managed via Django admin panel
- Responsive design
- Easy to customize and extend

---

## 🚀 Running the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/Abhishek-M-B/my_portfolio.git
cd my_portfolio
```

### 2. Create and activate a virtual environment

**Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**Mac/Linux:**
```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install django
```

> 💡 If a `requirements.txt` exists, use `pip install -r requirements.txt` instead.

### 4. Set up the database

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a superuser (for admin access)

```bash
python manage.py createsuperuser
```

### 6. Run the development server

```bash
python manage.py runserver
```

The project will be available at **http://localhost:8000**  
Admin panel: **http://localhost:8000/admin**

---

## 📁 Project Structure

```
my_portfolio/
├── manage.py
├── portfolio/          # Main app
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
├── static/             # CSS, JS, images
└── requirements.txt
```

---

## ☁️ Deploying to Railway

1. Push your code to GitHub
2. Go to [railway.app](https://railway.app) → **New Project** → **Deploy from GitHub**
3. Set environment variables in Railway dashboard:
   - `SECRET_KEY` = your Django secret key
   - `DEBUG` = `False`
   - `ALLOWED_HOSTS` = your Railway domain
4. Make sure your app listens on `PORT` from environment:
   ```python
   import os
   PORT = os.environ.get("PORT", 8000)
   ```
5. Add a `Procfile` in root:
   ```
   web: gunicorn your_project_name.wsgi
   ```

---

## 📬 Contact

**Abhishek M B**  
🔗 [GitHub](https://github.com/Abhishek-M-B)

---

> ⭐ If you found this helpful, consider giving the repo a star!
