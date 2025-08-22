# 🚖 Ride Hailing CLI (Python) · V1.0

> A fast, minimal, **pure‑Python** ride‑hailing experience that runs 100% **in‑memory**. Register riders & drivers, request/accept rides, manage vehicles, and track live statuses — all from your terminal.

<p align="center">
  <img alt="Python" src="https://img.shields.io/badge/Python-3.10%2B-blue" />
  <img alt="License" src="https://img.shields.io/badge/License-MIT-green" />
  <img alt="Status" src="https://img.shields.io/badge/Status-Active-brightgreen" />
</p>

---

## ✨ Highlights

* ⚡ **Zero setup**: no DB, no frameworks — just `python main.py`.
* 👥 **Role‑aware** flows for **Riders** and **Drivers**.
* 🚘 **Vehicle registry** tied to driver ownership.
* 📦 **In‑memory data** (clears on exit) — perfect for demos & learning.
* 🔁 **Ride lifecycle**: `requested → accepted → in_progress → completed/cancelled`.
* 🛡️ **Input validation** & friendly error messages.

---

## 📦 Quick Start

```bash
# 1) Clone
git clone https://github.com/<your-username>/ride-hailing-cli.git
cd ride-hailing-cli

# 2) (Optional) Create a virtual environment
python -m venv .venv && source .venv/bin/activate    # macOS/Linux
# or
python -m venv .venv && .venv\Scripts\activate       # Windows

# 3) Run
python main.py
```

> 💡 Everything runs in memory — closing the app resets all data.

---

## 🗂 Project Structure

```
ride_hailing_app/
│
├── main.py                 # Entry point for the CLI app
├── repositories/
│   ├── ride_repo.py        # RideRepository: manages rides in memory
│   ├── user_repo.py        # UserRepository: manages users in memory
│   └── vehicle_repo.py     # VehicleRepository: manages vehicles in memory
│
├── services/
│   ├── rides.py            # RideService: business logic for rides
│   ├── user.py             # UserManager: business logic for users
│   └── vehicle.py          # VehicleService: business logic for vehicles
│
└── README.md               # Project documentation
```

---

## 🧭 How It Works

* **Users** sign up as `Rider` or `Driver` and then log in.
* **Riders** can request a ride and monitor statuses.
* **Drivers** view open requests, accept and start rides, and mark completion.
* **Vehicles** can be registered/updated **only** by their owner drivers.

### Ride States

`requested → accepted → in_progress → completed` (or `cancelled` at any time before completion)

---

## 🖥️ CLI Walkthrough (Sample)

```text
Welcome to Ride Hailing CLI (V1.0)
1) Register
2) Login
3) Exit
> 1

Select role:
1) Rider
2) Driver
> 2
Enter name: Sanjana
Enter email: sanjana@example.com
Enter phone: +91-99999-99999
Set password: ******
✅ Driver registered! Please login.

> 2 (Login)
Email: sanjana@example.com
Password:
```
