# 🌐 Django REST Framework Learning Playground  

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)  
![Django](https://img.shields.io/badge/Django-4.x-green?logo=django)  
![DRF](https://img.shields.io/badge/DRF-3.x-red?logo=django)  
![License](https://img.shields.io/badge/License-MIT-yellow?logo=open-source-initiative)  

---

Welcome! 👋  
This repo is my **hands-on space for learning Django REST Framework (DRF)**.  
Think of it as a **lab notebook** — where I build APIs step by step, break things, fix them, and share what I learn 🚀.  

---

Here’s the current structure of my project:  

```
django-rest-api-learning/
├── backend/                # Main backend folder
│   ├── api/                # Django app for APIs
│   │   ├── migrations/     # Database migrations
│   │   ├── admin.py        # Admin panel config
│   │   ├── apps.py         # App configuration
│   │   ├── models.py       # Database models
│   │   ├── tests.py        # Unit tests
│   │   ├── urls.py         # API URLs
│   │   └── views.py        # API views (logic)
│   │
│   ├── cfehome/            # Main Django project
│   │   ├── settings.py     # Project settings
│   │   ├── urls.py         # Root URL configs
│   │   ├── wsgi.py         # WSGI config
│   │   └── asgi.py         # ASGI config
│   │
│   ├── db.sqlite3          # SQLite database (dev only)
│   └── manage.py           # Django management script
│
├── py_client/              # Python client for testing APIs
│   ├── basic.py
│   └── basic1.py
│
├── venv/                   # Virtual environment (ignored in git)
├── README.md               # Project documentation
└── requirements.txt        # Python dependencies
```

## ⚡ Getting Started  

Want to run this project locally? Follow these steps:  

```bash
# 1️⃣ Clone the repo
git clone https://github.com/<your-username>/django-rest-drf-playground.git
cd django-rest-drf-playground

# 2️⃣ Create a virtual environment
python -m venv venv

# Activate it
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Run migrations (set up database)
python manage.py migrate

# 5️⃣ Start the server
python manage.py runserver
Now open:
👉 Django Admin → http://127.0.0.1:8000/admin/
👉 API Playground → http://127.0.0.1:8000/api/

🎯 Learning Goals
By working on this repo, I aim to:

Build real-world REST APIs using Django REST Framework

Understand Serializers, ViewSets, Routers

Add Authentication & Permissions to secure APIs

Learn to document APIs properly

🤝 Contribute or Follow Along
This repo is mainly for my learning, but if you’re also starting with DRF:
