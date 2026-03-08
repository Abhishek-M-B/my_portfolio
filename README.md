# 🧑‍💻 My Personal Portfolio

A personal portfolio website built with **Django** — showcasing my projects, skills, and experience.

---

## 🌐 Live Demo

> 🚀 [View Portfolio](https://my-portfolio007.onrender.com/)

---

## 🛠️ Tech Stack

- **Backend:** Python, Django
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite (default)
- **Deployment:** Render

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
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux:**
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

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
├── portfolio/          # Django config (settings, urls, wsgi)
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── Base/               # Main app (views, models, templates)
│   ├── views.py
│   ├── models.py
│   └── templates/
├── static/             # CSS, JS, images
├── Procfile
└── requirements.txt
```

---

## ☁️ Deploying to Render (Free)

1. Push your code to GitHub
2. Go to [render.com](https://render.com) → **New** → **Web Service**
3. Connect your GitHub repo
4. Set the following:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python manage.py migrate && python manage.py collectstatic --noinput && gunicorn portfolio.wsgi`
5. Add environment variables in Render dashboard:
   - `SECRET_KEY` = your Django secret key
   - `DEBUG` = `False`
6. Add your Render URL to `ALLOWED_HOSTS` in `settings.py`:
   ```python
   RENDER_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
   if RENDER_HOSTNAME:
       ALLOWED_HOSTS.append(RENDER_HOSTNAME)
   ```
7. Click **Deploy** — your site will be live on a `.onrender.com` URL

> ⚠️ Free tier instances spin down after inactivity. The first visit after a period of inactivity may take ~50 seconds to load.

---

## 📬 Contact

**Abhishek M B**  
🔗 [GitHub](https://github.com/Abhishek-M-B)

---

> ⭐ If you found this helpful, consider giving the repo a star!
