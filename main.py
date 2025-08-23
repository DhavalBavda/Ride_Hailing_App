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
        print("2. View Ride By ID")
        print("3. View My Rides")
        print("4. Complete Ride")
        print("5. Cancel Ride")
        print("6. Logout")
    
    elif req == 3:
        print("\nRide Hailing App ------ Driver Menu")
        print("1. View Ride Requests")
        print("2. View My Rides")
        print("3. View Ride By ID")
        print("4. Accept Ride")
        print("5. Start Ride")
        print("6. Add Vehicle")
        print("7. View My Vehicles")
        print("8. Update Vehicle")
        print("9. Logout")
    
# Main function to run the application
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
            try:
                choice = int(input("Enter your choice: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

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
                    try:
                        driver_choice = int(input("Enter your choice: "))
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                        continue

                    # View ride requests
                    if driver_choice == 1:

                        rides = ride_service.list_rides() or []
                        if rides and len(rides) and any(ride.status == "requested" for ride in rides):
                            for ride in rides:
                                if ride.status == "requested":
                                    print(f"Ride ID: {ride.id}, Rider: {ride.rider_id}, Pickup: {ride.pickup}, Drop: {ride.drop}")
                                    print(f"Fare: {ride.fare}, Status: {ride.status}")
                        else:
                            print("No ride requests available.")

                    # View my rides
                    elif driver_choice == 2:
                        rides = ride_service.list_rides() or []
                        if rides and len(rides) and any(ride.driver_id == loggedInUser.id for ride in rides):
                            for ride in rides:
                                if ride.driver_id == loggedInUser.id:
                                    print(f"Ride ID: {ride.id}, Status: {ride.status}, Pickup: {ride.pickup}, Drop: {ride.drop}")
                                    print(f"Fare: {ride.fare}, Created At: {ride.created_at}")
                        else:
                            print("No rides found.")
                    
                    # View ride by ID
                    elif driver_choice == 3:

                        ride_id = input("Enter Ride ID to view: ")
                        ride = ride_service.view_ride(ride_id)
                        if ride:
                            print(f"Ride ID: {ride.id}, Status: {ride.status}, Rider: {ride.rider_id}, Pickup: {ride.pickup}, Drop: {ride.drop}")
                            print(f"Fare: {ride.fare}, Created At: {ride.created_at}")
                        else:
                            print("Ride not found.")

                    # Accept ride
                    elif driver_choice == 4:
                        rides = ride_service.list_rides() or []
                        if rides:
                            for ride in rides:
                                if ride.status == "requested":
                                    print(f"Ride ID: {ride.id}, Rider: {ride.rider_id}, Pickup: {ride.pickup}, Drop: {ride.drop}")
                                    print(f"Fare: {ride.fare}, Status: {ride.status}")
                            
                            ride_id = input("Enter Ride ID to accept: ")
                            ride = ride_service.accept_ride(ride_id, loggedInUser.email)
                            if ride:
                                print(f"Ride {ride.id} accepted.")
                            else:
                                print("Ride not found.")
                        else:
                            print("No ride requests available.")
                    
                    # Start ride
                    elif driver_choice == 5:

                        ride_id = input("Enter Ride ID to start: ")
                        ride = ride_service.start_ride(ride_id)
                        if ride:
                            print(f"Ride {ride.id} started.")
                        else:
                            print("Ride not found.")

                    # Add vehicle
                    elif driver_choice == 6:

                        driver_id = loggedInUser.id
                        print("Enter vehicle details:")
                        brand = input("Enter vehicle brand: ")
                        model = input("Enter vehicle model: ")
                        year = input("Enter vehicle year: ")
                        plate_number = input("Enter vehicle plate number: ")
                        color = input("Enter vehicle color: ")
                        vehicle = vehicle_service.register_vehicle(driver_id, brand, model, year, plate_number, color)
                        if vehicle : 
                            print(f"Vehicle {vehicle.plate_number} registered successfully.")
                    
                    # View my vehicles
                    elif driver_choice == 7:
                        vehicles = vehicle_service.get_all_vehicles() or []
                        if vehicles:
                            for vehicle in vehicles:
                                if vehicle.driver_id == loggedInUser.id:
                                    print(f"Vehicle ID: {vehicle.id}, Brand: {vehicle.brand}, Model: {vehicle.model}, Year: {vehicle.year}, Plate Number: {vehicle.plate_number}, Color: {vehicle.color}")
                        else:
                            print("No vehicles found.")
                    
                    # Update vehicle
                    elif driver_choice == 8:

                        vehicle_id = input("Enter Vehicle ID to update: ")
                        vehicle = vehicle_service.get_vehicle_by_id(vehicle_id)
                        if not vehicle:
                            print("Vehicle not found.")
                            continue
                        if vehicle.driver_id != loggedInUser.id:
                            print("You can only update your own vehicles.")
                            continue
                        
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
                            print("Vehicle not updated.")
                    
                    elif driver_choice == 9:

                        print("Logging out...")
                        loggedInUser = None
                        break

                    else:
                        print("Invalid choice. Please try again.")

            elif role == "Rider":
                while True:
                    showMenu(2)
                    try:
                        rider_choice = int(input("Enter your choice: "))
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                        continue

                    # Request ride
                    if rider_choice == 1:

                        pickup = input("Enter pickup location: ")
                        drop = input("Enter drop location: ")
                        ride = ride_service.request_ride(loggedInUser.email, pickup, drop)
                        if ride:
                            print(f"Ride {ride.id} created successfully.")
                        else:
                            print("No drivers available at the moment.")
                    
                    # View ride by ID
                    elif rider_choice == 2:
                        ride_id = input("Enter Ride ID to view: ")
                        ride = ride_service.view_ride(ride_id)
                        if ride:
                            print(f"Ride ID: {ride.id}, Status: {ride.status}, Driver: {ride.driver_id}, Pickup: {ride.pickup}, Drop: {ride.drop}")
                        else:
                            print("Ride not found.")

                    # My Rides
                    elif rider_choice == 3:
                        rides = ride_service.list_rides() or []
                        if rides:
                            for ride in rides:
                                if ride.rider_id == loggedInUser.id:
                                    # Display rides for the logged-in user
                                    print(f"Ride ID: {ride.id}, Status: {ride.status}")
                                    print(f"Pickup: {ride.pickup}, Drop: {ride.drop}, Fare: {ride.fare}")
                        else:
                            print("No rides found.")

                    # Complete Ride
                    elif rider_choice == 4:

                        ride_id = input("Ride ID: ")
                        ride = ride_service.complete_ride(ride_id)
                        if ride:
                            print(f"Ride {ride.id} completed.")
                        else:
                            print("Ride not found.")

                    # Cancel Ride
                    elif rider_choice == 5:
                        
                        ride_id = input("Ride ID: ")
                        ride = ride_service.cancel_ride(ride_id)
                        if ride:
                            print(f"Ride {ride.id} cancelled.")
                        else:
                            print("Ride not found.")
                        
                    elif rider_choice == 6:
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
    
