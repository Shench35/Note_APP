# 📝 My Notes App

A simple, fast, and intuitive personal note-taking web application built with FastAPI. No signup required - just start writing!

[![Live Demo](https://img.shields.io/badge/demo-live-success)](https://note-app-u1m0.onrender.com)
[![Python](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)](https://fastapi.tiangolo.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 🌐 Live Demo

**[Try it live here!](https://note-app-u1m0.onrender.com)**

> ⚠️ **Note:** First load may take 30-60 seconds as the server spins up (Render free tier limitation).

---

## 📖 About The Project

My Notes App is a lightweight, session-based note-taking application that allows users to create and manage personal notes without the hassle of creating an account. Each user gets a unique session that persists for 10 years, making it perfect for quick note-taking and personal organization.

This project was built as a learning exercise to understand:
- FastAPI web framework fundamentals
- Session management and cookie handling
- File-based data persistence
- Full-stack web development
- Cloud deployment workflows

### Why This Project?

Traditional note-taking apps often require lengthy signup processes. This app provides instant access - just visit the site and start writing. It's perfect for:
- Quick temporary notes
- Personal task lists
- Draft ideas and thoughts
- Learning web development concepts

---

## ✨ Features

### Current Features
✅ **Instant Access** - No signup or login required  
✅ **Create Notes** - Add new notes with a simple, clean interface  
✅ **Edit Notes** - Modify existing notes anytime  
✅ **Persistent Sessions** - Your notes stay available for 10 years via secure cookies  
✅ **Privacy First** - Each user has a unique session ID, notes are private  
✅ **Responsive Design** - Clean, minimal interface  
✅ **Fast & Lightweight** - JSON-based storage for quick operations  

### Coming Soon
🚧 **Delete Notes** - Remove unwanted notes  
🚧 **Note Categories** - Organize notes with tags  
🚧 **Search Functionality** - Find notes quickly  
🚧 **Export Notes** - Download your notes in various formats  
🚧 **Dark Mode** - Easy on the eyes  

---

## 🛠️ Built With

- **Backend Framework:** [FastAPI](https://fastapi.tiangolo.com/) - Modern, fast Python web framework
- **Template Engine:** [Jinja2](https://jinja.palletsprojects.com/) - Powerful templating for Python
- **Session Management:** [Starlette SessionMiddleware](https://www.starlette.io/) - Secure cookie-based sessions
- **Data Storage:** JSON file-based persistence
- **Frontend:** HTML5, CSS3 (vanilla)
- **Deployment:** [Render](https://render.com/) - Cloud platform for modern apps
- **Environment Management:** [python-dotenv](https://pypi.org/project/python-dotenv/) - Secure configuration

---

## 🚀 Getting Started

Follow these steps to run the project locally on your machine.

### Prerequisites

- Python 3.11 or higher
- pip (Python package manager)
- Git

### Installation

1. **Clone the repository**
```bash
   git clone https://github.com/shench35/note-app.git
   cd note-app
```

2. **Create a virtual environment (recommended)**
```bash
   # On Windows
   python -m venv venv
   venv\Scripts\activate

   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
```

3. **Install dependencies**
```bash
   pip install -r requirements.txt
```

4. **Set up environment variables**
   
   Create a `.env` file in the root directory:
```bash
   # Generate a secure secret key first
   python -c "import secrets; print('SECRET_KEY=JESUS_IS_LORD' + secrets.token_hex(32))"
```
   
   Copy the output and create `.env`:
```env
   SECRET_KEY=JESUS_IS_LORD[your_generated_key_here]
```

   > ⚠️ **Important:** Never commit your `.env` file to Git. It's already in `.gitignore`.

5. **Initialize the notes database**
   
   Create an empty `notes.json` file:
```bash
   # On Windows
   echo {} > notes.json

   # On macOS/Linux
   echo '{}' > notes.json
```

6. **Run the application**
```bash
   uvicorn main:app --reload
```

7. **Open your browser**
   
   Navigate to: `http://127.0.0.1:8000`

---

## 📖 Usage

### Adding a Note
1. Visit the home page
2. Type your note in the textarea
3. Click the "➕ Add Note" button
4. Your note appears instantly below

### Editing a Note
1. Click the "Edit" button on any note
2. Modify the text in the edit page
3. Click "Update Note" to save changes
4. You'll be redirected back to the home page

### Session Persistence
- Your session lasts for **10 years** via secure cookies
- Close your browser and return anytime - your notes will be there
- Each browser/device gets a unique session
- Clearing cookies will create a new session (notes from old session won't be accessible)

---

## 📁 Project Structure
```
note-app/
│
├── main.py                 # FastAPI application and all routes
├── templates/              # HTML templates
│   ├── index.html         # Main notes page (view/add notes)
│   └── edit.html          # Note editing page
├── static/                 # Static assets
│   └── styles.css         # Application styles
├── notes.json             # JSON database (auto-created, stores all notes)
├── .env                   # Environment variables (CREATE THIS - not in git)
├── .gitignore            # Git ignore rules
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

### Key Files Explained

- **`main.py`** - Contains all application logic, routes, and endpoints
- **`templates/`** - Jinja2 HTML templates for rendering pages
- **`static/`** - CSS and other static files
- **`notes.json`** - Stores all user notes in JSON format (auto-created on first note)
- **`.env`** - Contains sensitive configuration (you must create this)

---

## ⚙️ Configuration

### Environment Variables

The application requires a `SECRET_KEY` for secure session management.

**To generate a secure secret key:**
```python
import secrets
print("JESUS_IS_LORD" + secrets.token_hex(32))
```

**Create `.env` file:**
```env
SECRET_KEY=JESUS_IS_LORD[paste_your_generated_key_here]
```

### Session Configuration

Sessions are configured with:
- **Lifetime:** 10 years (315,360,000 seconds)
- **Storage:** Secure HTTP-only cookies
- **Scope:** Per-browser/device

---

## 🔍 How It Works

### Session Management
1. When you first visit the site, a unique `user_id` is generated
2. This ID is stored in a secure cookie that lasts 10 years
3. All your notes are associated with this `user_id`
4. The cookie survives browser restarts but not cookie clearing

### Data Storage
```json
{
  "user_id_1": [
    {"id": 1, "content": "First note"},
    {"id": 2, "content": "Second note"}
  ],
  "user_id_2": [
    {"id": 1, "content": "Another user's note"}
  ]
}
```

- Each user has their own array of notes
- Notes are identified by sequential IDs
- The entire structure is saved to `notes.json`

### Request Flow

**Adding a Note:**
```
User submits form → POST /add-note → Read notes.json → 
Add new note to user's array → Save to notes.json → 
Redirect to home page
```

**Editing a Note:**
```
User clicks Edit → GET /edit-note/{id} → Load note content → 
Show edit form → User submits → POST /edit-note → 
Find note by ID → Update content → Save → Redirect home
```

---

## 🚧 Known Issues & Limitations

### Current Limitations
- **No multi-device sync** - Sessions are browser-specific
- **Cookie dependency** - Clearing cookies = losing access to notes
- **No backup system** - Notes only exist in `notes.json`
- **Single file storage** - Not suitable for thousands of users
- **No authentication** - Anyone with your session cookie can access your notes

### Deployment Considerations
- **Render free tier** - App sleeps after 15 minutes of inactivity
- **Cold start time** - First request may take 30-60 seconds
- **File persistence** - Render's ephemeral filesystem means notes may be lost on redeploy

> 💡 **For production use**, consider migrating to a proper database (PostgreSQL, MongoDB) and adding authentication.

---

## 🗺️ Roadmap

### Phase 1: Core Features (Completed)
- [x] Basic note creation
- [x] Note editing
- [x] Session management
- [x] Deployment to Render

### Phase 2: Enhanced Functionality (In Progress)
- [ ] Delete note feature
- [ ] Note search
- [ ] Categories/tags
- [ ] Export functionality

### Phase 3: Advanced Features (Planned)
- [ ] User authentication (optional login)
- [ ] Multi-device sync
- [ ] Rich text editor
- [ ] Note sharing
- [ ] Dark mode
- [ ] Database migration (PostgreSQL)

---

## 🤝 Contributing

This is a learning project, but contributions, issues, and feature requests are welcome!

### Reporting Bugs

Found a bug? Please [open an issue](https://github.com/shench35/note-app/issues) with:
- Clear description of the bug
- Steps to reproduce
- Expected vs actual behavior
- Screenshots (if applicable)
- Your browser and OS

### Suggesting Features

Have an idea? [Open an issue](https://github.com/shench35/note-app/issues) with the `enhancement` label:
- Describe the feature
- Explain why it would be useful
- Suggest how it might work

### Pull Requests

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📚 What I Learned

Building this project taught me valuable skills:

### Technical Skills
- **FastAPI fundamentals** - Routing, request handling, form processing
- **Session management** - Cookie-based authentication, security considerations
- **Template rendering** - Jinja2 templating, passing data to frontend
- **File I/O in Python** - Reading/writing JSON, data persistence
- **Deployment** - Environment variables, production configuration, Render platform
- **Version control** - Git workflows, `.gitignore` best practices

### Development Practices
- **Security awareness** - Secret key management, session security
- **Code organization** - Separating concerns, clean structure
- **Error handling** - Graceful failures, user feedback
- **Documentation** - Writing clear, helpful README files

### Challenges Overcome

1. **Session Persistence Challenge**
   - Problem: Sessions expiring on browser close
   - Solution: Configured `max_age` parameter for long-lived cookies

2. **Data Structure Design**
   - Problem: Efficiently storing multi-user notes
   - Solution: Nested JSON structure with user IDs as keys

3. **Form Handling**
   - Problem: Button outside form tags not submitting
   - Solution: Proper HTML structure understanding and debugging

4. **Deployment Configuration**
   - Problem: Secret key changing on server restart
   - Solution: Environment variables and persistent configuration

---

## 📸 Screenshots

### Home Page
![Home Page](screenshots/home.png)
*Main interface showing all notes with add functionality*

### Edit Note
![Edit Note](screenshots/edit.png)
*Clean edit interface for modifying existing notes*

> 📷 *Add screenshots to `screenshots/` folder in your repository*

---

## 🔐 Security Notes

- **Secret keys** are stored in `.env` and never committed to Git
- **Session cookies** are HTTP-only and secure
- **User isolation** prevents users from accessing each other's notes
- **No sensitive data** should be stored (app is for learning purposes)

### Security Recommendations
- Regenerate `SECRET_KEY` for production deployments
- Use HTTPS in production (Render provides this automatically)
- Implement rate limiting for production use
- Add CSRF protection for forms
- Consider adding user authentication for sensitive data

---

## 📄 License

This project is licensed under the MIT License.
```
MIT License

Copyright (c) 2025 shench35

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 👤 Author

**GitHub:** [@shench35](https://github.com/shench35)  
**Project Link:** [https://github.com/shench35/note-app](https://github.com/shench35/note-app)  
**Live Demo:** [https://note-app-u1m0.onrender.com](https://note-app-u1m0.onrender.com)

---

## 🙏 Acknowledgments

- [FastAPI Documentation](https://fastapi.tiangolo.com/) - Excellent framework documentation
- [Render](https://render.com/) - Free hosting platform for learning projects
- [Python.org](https://www.python.org/) - Python programming language
- [Stack Overflow](https://stackoverflow.com/) - Community support and problem-solving

---

## 📞 Support

If you found this project helpful, please consider:
- ⭐ Starring the repository
- 🐛 Reporting bugs
- 💡 Suggesting new features
- 🔀 Contributing code

---

**Happy Note-Taking! 📝**

*Built with ❤️ and Python*
