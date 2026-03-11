# 🐍 Python Admin Web

A simple **web administration interface built with Flask** for basic user management.

This project was developed as a learning exercise to explore the fundamentals of **Python web development**, including routing, templates, form handling, and data persistence using JSON.

The application provides a minimal interface to **manage users stored locally** and demonstrates how a lightweight backend can power a functional web interface.

---

## ✨ Features

🔐 Simple login system  
👤 User registration  
📋 User listing and management  
💾 Local data storage using JSON  
🧩 HTML templates rendered with Jinja2  
🌐 Lightweight Flask web server  

---

## 🛠️ Technologies Used

- **Python**
- **Flask**
- **HTML**
- **Jinja2 Templates**
- **JSON** for local data persistence

---

## 📁 Project Structure

```
Python_Admin_Web/
│
├── app.py
├── usuarios.json
├── requirements.txt
├── README.md
│
└── templates/
    ├── index.html
    ├── login.html
    └── usuarios.html
```

- **app.py** → main Flask application  
- **usuarios.json** → local storage for user data  
- **templates/** → HTML templates rendered by Flask  

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/ElyonKyla/Python_Admin_Web
cd Python_Admin_Web
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

The server will start at:

```
http://127.0.0.1:5000
```

---

## 📚 Educational Purpose

This project was created for **learning purposes** to practice:

- Flask web development
- backend logic with Python
- template rendering with Jinja2
- simple user management workflows
- JSON-based data persistence

It is not intended for production use.

---

## 📄 License

This project is distributed under the **MIT License**.

---

⭐ If you find this project interesting, feel free to explore the code and experiment with it.
