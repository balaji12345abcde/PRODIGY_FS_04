# PRODIGY_FS_04
Here’s a **GitHub-ready README.md** for your **Task-04: Real-Time Chat Application** using **Django Channels, Daphne, HTML, CSS, and JavaScript**:

---

# 📨 Real-Time Chat Application

This project is a **real-time chat application** built with **Django Channels** and **WebSockets** to enable instant messaging between users. It supports **user authentication, chat rooms, private messaging**, and can be extended with optional features like **chat history, notifications, and file sharing**.

---

## 🚀 Features

✅ User signup, login, and logout
✅ Real-time messaging using **WebSockets**
✅ Create or join chat rooms
✅ Private one-to-one conversations
✅ Online user presence indicators
✅ Chat history storage in database
✅ Responsive UI with **HTML, CSS, and JavaScript**
✅ Powered by **Daphne ASGI server**

---

## 🛠️ Tech Stack

* **Backend:** Django, Django Channels, Daphne
* **Frontend:** HTML, CSS, JavaScript
* **WebSockets:** Django Channels
* **Database:** SQLite (default, can be changed to PostgreSQL/MySQL)

---

## 📂 Project Structure

```
chat_app/
│── chat/                  # Chat application (models, views, consumers, routing)
│── accounts/              # User authentication (signup, login, logout)
│── chat_app/              # Main project (settings, ASGI, URLs)
│── templates/             # HTML templates
│── static/                # CSS & JS files
│── manage.py
```

---

## ⚡ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/real-time-chat-app.git
cd real-time-chat-app
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run Database Migrations

```bash
python manage.py migrate
```

### 5️⃣ Create Superuser (Admin)

```bash
python manage.py createsuperuser
```

### 6️⃣ Run the Development Server with **Daphne**

```bash
daphne -p 8000 chat_app.asgi:application
```

Now open your browser at:
👉 [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🖥️ Usage

1. Register a new account or login with existing credentials.
2. Create or join a chat room.
3. Start real-time conversations with other users.
4. Optionally enable **private messaging, notifications, and file sharing**.

---

## 📸 Screenshots

![Image](https://github.com/user-attachments/assets/0dc01867-95c5-4d2c-af25-9c513f6bea99)
![Image](https://github.com/user-attachments/assets/973b6fd2-b8f4-4b73-bbf9-d8b69fc19e5b)

![Image](https://github.com/user-attachments/assets/08d7da66-4eca-429b-988a-86335e13d6cf)
![Image](https://github.com/user-attachments/assets/650bf058-45a5-47ca-a733-3a3ae45a37bc)
![Image](https://github.com/user-attachments/assets/7d80038d-4bfd-4021-aac6-b4a26d884b51)

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---

## 📜 License

This project is licensed under the **MIT License** – feel free to use and modify.

---

⚡ **Developed as part of Task-04 Internship Project (Prodigy Infotech)**
