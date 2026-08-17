🔐 Secure Login System
A simple and secure user authentication web application built using Python, Flask, SQLite, HTML, and CSS.
✨ Features
🔑 User registration and login
🔒 Secure password hashing
🗄️ SQLite database integration
🛡️ Session-based authentication
🚪 Logout functionality
📊 Protected user dashboard
⚠️ Invalid login handling
🎨 Clean dark-themed user interface
📱 Responsive design
🛠️ Technologies Used
Python
Flask
SQLite
HTML5
CSS3
Werkzeug
📂 Project Structure
secure-login-system/
│
├── app.py
├── README.md
├── .gitignore
│
└── templates/
    ├── login.html
    ├── register.html
    └── dashboard.html
🚀 How to Run
1. Install Flask
pip install flask
2. Run the application
python app.py
3. Open in your browser
http://127.0.0.1:5000
🔐 Security
Passwords are not stored as plain text. They are hashed using Werkzeug's password-hashing functions before being stored in the SQLite database.
The database file is excluded from the GitHub repository using .gitignore.
🎯 Project Purpose
This project was developed to understand the fundamentals of:
Web authentication
Password security
Database management
Session handling
Flask web development
👨‍💻 Author
Mohamed Yacoof Mursith
📌 Note
This project is intended for educational purposes and demonstrates the basic concepts of secure authentication in a Flask application.
