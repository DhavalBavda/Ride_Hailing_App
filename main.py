from repositories.ride_repo import RideRepository
from repositories.user_repo import UserRepository
from repositories.vehicle_repo import VehicleRepository
from services.user import UserManager
from services.rides import RideService
from services.vehicle import VehicleService

def showMenu(req):
    if req == 1:
        print("\nRide Hailing App ------ Main Menu")
        print("1. Register User")
        print("2. Login User")
        print("3. Exit")
    elif req == 2:
        print("\nRide Hailing App ------ Rider Menu")
        print("1. Request Ride")
        print("2. Complete Ride")
        print("3. Cancel Ride")
        print("4. View Rides")
        print("5. Logout")
    elif req == 3:
        print("\nRide Hailing App ------ Driver Menu")
        print("1. View Ride Requests")
        print("2. Start Ride")
        print("3. Add Vehicle")
        print("4. Update Vehicle")
        print("5. Logout")


def main():

    # Initialize Repositories
    user_repo = UserRepository()
    vehicle_repo = VehicleRepository()
    ride_repo = RideRepository()

    user_manager = UserManager(user_repo)
    ride_service = RideService(ride_repo, user_repo, vehicle_repo)
    vehicle_service = VehicleService(vehicle_repo)

    loggedInUser = None  # keeps track of active user

    while True:
        if not loggedInUser:
            # Show main menu if no user is logged in
            showMenu(1)
            choice = int(input("Enter your choice: "))

            if choice == 1:  # Register
                loggedInUser = user_manager.create_user()
            elif choice == 2:  # Login
                loggedInUser = user_manager.login_user()
            elif choice == 3:   
                print("Exiting the application. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
                continue
        else:
            # User is logged in, check role
            role = loggedInUser.get_role()

            if role == "Driver":
                while True:
                    showMenu(3)
                    driver_choice = int(input("Enter your choice: "))
                    if driver_choice == 1:

                        print("Viewing ride requests... (Functionality to be implemented)")
                    elif driver_choice == 2:

                        ride_id = input("Enter Ride ID to start: ")
                        ride = ride_service.start_ride(ride_id)
                        if ride:
                            print(f"Ride {ride.ride_id} started.")
                        else:
                            print("Ride not found.")

                    elif driver_choice == 3:

                        driver_id = loggedInUser.id
                        brand = input("Enter vehicle brand: ")
                        model = input("Enter vehicle model: ")
                        year = input("Enter vehicle year: ")
                        plate_number = input("Enter vehicle plate number: ")
                        color = input("Enter vehicle color: ")
                        vehicle = vehicle_service.register_vehicle(driver_id, brand, model, year, plate_number, color)
                        print(f"Vehicle {vehicle.plate_number} registered successfully.")

                    elif driver_choice == 4:
                        vehicle_id = input("Enter Vehicle ID to update: ")
                        print("Enter new details (leave blank to keep current value):")
                        brand = input("New Brand: ")
                        model = input("New Model: ")
                        year = input("New Year: ")
                        plate_number = input("New Plate Number: ")
                        color = input("New Color: ")
                        updates = {k: v for k, v in {
                            "brand": brand,
                            "model": model,
                            "year": year,
                            "plate_number": plate_number,
                            "color": color
                        }.items() if v}
                        updated_vehicle = vehicle_service.update_vehicle_info(vehicle_id, **updates)
                        if updated_vehicle:
                            print(f"Vehicle {updated_vehicle.plate_number} updated successfully.")
                        else:
                            print("Vehicle not found.")
                    
                    elif driver_choice == 5:

                        print("Logging out...")
                        loggedInUser = None
                        break

                    else:
                        print("Invalid choice. Please try again.")

            elif role == "Rider":
                while True:
                    showMenu(2)
                    rider_choice = int(input("Enter your choice: "))

                    if rider_choice == 1:

                        pickup = input("Enter pickup location: ")
                        drop = input("Enter drop location: ")
                        ride = ride_service.request_ride(loggedInUser.user_id, pickup, drop)
                        if ride:
                            print(f"Ride {ride.ride_id} created successfully.")
                        else:
                            print("No drivers available at the moment.")
                    
                    elif rider_choice == 2:

                        ride_id = input("Ride ID: ")
                        ride = ride_service.complete_ride(ride_id)
                        if ride:
                            print(f"Ride {ride.ride_id} completed.")
                        else:
                            print("Ride not found.")

                    elif rider_choice == 3:
                        
                        ride_id = input("Ride ID: ")
                        ride = ride_service.cancel_ride(ride_id)
                        if ride:
                            print(f"Ride {ride.ride_id} cancelled.")
                        else:
                            print("Ride not found.")
                        
                    elif rider_choice == 4:
                        print("Viewing rides... (Functionality to be implemented)")
                    elif rider_choice == 5:
                        print("Logging out...")
                        loggedInUser = None
                        break
                    else:
                        print("Invalid choice. Please try again.")

            else:
                print("Invalid role selected during registration.")
                loggedInUser = None  # Reset session

if __name__ == "__main__":
    main()
