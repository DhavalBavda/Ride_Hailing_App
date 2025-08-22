# 🚖 Ride Hailing CLI App in Python (V1.0)

![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Repo Stars](https://img.shields.io/github/stars/ArjunPraja/Ride_Hailing_App?style=social)
![Contributors](https://img.shields.io/github/contributors/ArjunPraja/Ride_Hailing_App)
![Open Issues](https://img.shields.io/github/issues/ArjunPraja/Ride_Hailing_App)

> 🚀 A powerful command-line Ride Hailing app built with **pure Python**.
> Riders & Drivers can register, request rides, manage vehicles, and track rides in real-time – all **in-memory** without any database.

---

## ✨ Features

### 👤 User Management

* ✅ Register as Rider or Driver
* ✅ Login for existing users
* ✅ Role-based menus & actions

### 🚗 Rider Features

* ✅ Request a ride
* ✅ View ride by ID
* ✅ View all my rides
* ✅ Complete a ride
* ✅ Cancel a ride

### 🛻 Driver Features

* ✅ View ride requests
* ✅ Accept rides
* ✅ Start rides
* ✅ View ride by ID
* ✅ Add or update vehicles

### 🚙 Vehicle Management

* ✅ Register new vehicles
* ✅ Update existing vehicle information
* ✅ Only owners can update vehicles

### 📍 Ride Management

* ✅ List all rides
* ✅ Track ride status: `requested`, `accepted`, `in_progress`, `completed`, `cancelled`

---

## 📂 Project Structure

```
ride_hailing_app/
│── Models/
│   ├── User_model.py       # Defines user schema and methods
│   ├── Vehicles_model.py   # Defines vehicle schema and logic
│   └── Rides_model.py      # Defines ride schema and logic
│
├── main.py                 # Entry point for the CLI app
│
├── repositories/
│   ├── ride_repo.py        # Manages rides in memory
│   ├── user_repo.py        # Manages users in memory
│   └── vehicle_repo.py     # Manages vehicles in memory
│
├── services/
│   ├── rides.py            # Business logic for rides
│   ├── user.py             # Business logic for users
│   └── vehicle.py          # Business logic for vehicles
|
├── utils/
│   ├── helper.py           # Helper functions
│
└── README.md               # Documentation
```

---

## 🏗 Architecture

```
      ┌───────────┐        ┌────────────┐        ┌─────────────┐
      │   Models  │ -----> │ Repositories│ -----> │   Services  │
      └───────────┘        └────────────┘        └─────────────┘
            ↑                                               │
            └────────────────────── main.py ───────────────┘
```

* **Models** → Define data (`User`, `Vehicle`, `Ride`)
* **Repositories** → Store and retrieve data (in-memory)
* **Services** → Business logic & validations
* **main.py** → CLI interface

---

## ⚡ Quickstart

1️⃣ Clone the repo:

```bash
git clone https://github.com/ArjunPraja/Ride_Hailing_App.git
cd Ride_Hailing_App
```

2️⃣ Run the app:

```bash
python main.py
```

3️⃣ Follow the CLI menu to register, request rides, and manage vehicles 🚖

---

## 🛠 Technologies Used

* 🐍 Python 3.x
* 🧩 Object-Oriented Programming (OOP)
* 🗂 In-memory data storage (Python dictionaries)
* 💻 Command-Line Interface (CLI)

---

## 📌 Notes

⚡ All data is **temporary** (cleared when program exits)
⚡ Built-in **input validation & error handling**
⚡ Future-ready: Can be extended to DB, REST API, or GUI

---

## 🚀 Roadmap

* [ ] Add persistent database (SQLite / MongoDB)
* [ ] Build REST API with FastAPI
* [ ] Add authentication & JWT tokens
* [ ] Web Dashboard (React / Vue)
* [ ] Unit tests for services

---

## 👨‍💻 Contributors

| [Dhaval Bavda](https://github.com/DhavalBavda)                    | [Sanjana](https://github.com/SanjanaV5103)                        | [Janhawi K ](https://github.com/JK-3)                       | [Arjun Prajapati](https://github.com/ArjunPraja)                  |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| ![](https://avatars.githubusercontent.com/u/110212178?v=4\&s=100) | ![](https://avatars.githubusercontent.com/u/119767158?v=4\&s=100) | ![](https://avatars.githubusercontent.com/u/112979657?v=4\&s=100) | ![](https://avatars.githubusercontent.com/u/119833180?v=4\&s=100) |
