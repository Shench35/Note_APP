.

📝 FastAPI Notes App

A simple notes web application built with FastAPI, Jinja2, HTML, and CSS.
Users can write notes and submit them using a form. Notes are stored in memory and displayed on the page.

⚠️ This project is for learning purposes. Notes are not persisted and will reset when the server restarts.

🚀 Features

Create notes using a web form

Display all added notes on the same page

Server-side rendering with Jinja2 templates

FastAPI backend

No database (in-memory storage)

Simple and clean UI

🛠️ Technologies Used

Python

FastAPI

Jinja2

HTML

CSS

Uvicorn

📁 Project Structure

Note_APP/
│
├── main.py
├── requirements.txt
├── templates/
│   └── index.html
├── static/
│   └── styles.css
└── README.md


⚙️ Installation & Setup (Local)
1️⃣ Clone the repository

git clone https://github.com/YOUR_USERNAME/note-app.git
cd note-app

2️⃣ Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate      # On Linux/Mac
venv\Scripts\activate         # On Windows


3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Run the application
uvicorn main:app --reload

🧠 How It Works (Concept)

The frontend sends a POST request when a note is added.

FastAPI receives the form data.

Notes are stored in a Python list (in memory).

The page reloads and Jinja2 renders all notes dynamically.

⚠️ Limitations

Notes are not persistent

Server restarts clear all notes

No authentication or database

🔮 Possible Improvements

Add SQLite or another database

Add delete and edit note functionality

Use JavaScript (AJAX) to avoid page reload

Improve UI/UX

Add user authentication

👤 Author

Akinpelu Shuaib

Learning backend development with FastAPI

Exploring full-stack web development

📜 License

This project is open-source and free to use for learning and educational purposes.