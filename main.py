from repositories.ride_repo import RideRepository
from repositories.user_repo import UserRepository
from repositories.vehicle_repo import VehicleRepository
from services.user import UserManager

def main():

    # Initialize Repositories
    user_repo = UserRepository()
    vehicle_repo = VehicleRepository()
    ride_repo = RideRepository()

    user_manager = UserManager(user_repo)

    while True:
        print("\nRide Hailing App ------ Main Menu")
        print("1. Register User")
        print("2. Login User")
        print("3. Exit")

        choice  = int(input("Enter your choice: "))

        if choice == 1:
            loggedInUser = user_manager.create_user()
            
            continue  # Registration logic here
        elif choice == 2:
            user_manager.login_user()
            continue  # Login logic here
        elif choice == 3:   
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()

