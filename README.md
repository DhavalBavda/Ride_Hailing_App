# Ride Hailing CLI App in Python (V1.0)

A command-line based Ride Hailing application written in **pure Python**, which maintains all data in memory (no database). Users can register as **Riders** or **Drivers**, request rides, manage vehicles, and track ride statuses in real-time during the application session. Once the application exits, all data is cleared.

---

## Features

### User Management

* Register new users (Rider or Driver)
* Login for existing users
* Role-based menus and actions

### Rider Features

* Request a ride
* View ride by ID
* View all my rides
* Complete a ride
* Cancel a ride

### Driver Features

* View ride requests
* Accept rides
* Start rides
* View ride by ID
* Add or update vehicles

### Vehicle Management

* Register new vehicles
* Update existing vehicle information
* Restrict updates to owner drivers only

### Ride Management

* List all rides
* Track ride status: `requested`, `accepted`, `in_progress`, `completed`, `cancelled`

---

## Project Structure

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

## How to Run

1. Clone the repository:

```bash
gh repo clone ArjunPraja/Ride_Hailing_App
cd ride-hailing-cli
```

2. Run the application:

```bash
python main.py
```

3. Follow the on-screen CLI menus to register users, request rides, manage vehicles, and perform ride actions.

---

## Technologies Used

* Python 3.x
* Object-Oriented Programming (OOP)
* In-memory data management using Python dictionaries
* Command-line interface (CLI)

---

## Notes

* All data is **temporary** and stored in memory only during runtime. Exiting the program clears all users, rides, and vehicles.
* Input validation and exception handling are implemented to prevent crashes from invalid operations or missing data.
* The project can be extended to add persistence via a database or a web interface in the future.

## Contributors

* **Dhaval Bavda** - [GitHub](https://github.com/DhavalBavda)
* **Arjun Prajapati** - [GitHub](https://github.com/ArjunPraja)
* **Sajana** - [GitHub](https://github.com/SanjanaV5103)
* **Janhwi** - [GitHub](https://github.com/JK-3)
