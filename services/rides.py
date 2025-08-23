from Models.rides_model import RidesModel
from repositories.ride_repo import RideRepository
from repositories.user_repo import UserRepository
from repositories.vehicle_repo import VehicleRepository
from utils.helper import HelperFunctions as HF 
import uuid 

class RideService:
        def __init__(self, ride_repo: RideRepository, user_repo: UserRepository, vehicle_repo: VehicleRepository):
            self.ride_repo = ride_repo
            self.user_repo = user_repo
            self.vehicle_repo = vehicle_repo
        
        @HF.safe_action_decorator
        def request_ride(self, rider_email: str, pickup: str, drop: str):
            rider = self.user_repo.get_user_by_email(rider_email)
            if not rider:
                raise ValueError("Invalid rider")

            fare = 100  

            # Correct argument order
            ride = RidesModel(
                rider_id=rider.id,
                driver_id=None,
                pickup=pickup,
                drop_location=drop,
                status="requested",
                fare=fare
            )

            self.ride_repo.add_ride(ride)
            return ride
        
        @HF.safe_action_decorator
        def accept_ride(self, ride_id: str, driver_email: str):
            ride = self.ride_repo.get_ride(ride_id)
            driver = self.user_repo.get_user_by_email(driver_email)
            if not ride or not driver:
                raise ValueError("Invalid ride or driver")
            if ride.driver_id is not None:
                raise ValueError("Ride already accepted by another driver")
            ride.driver_id = driver.id
            ride.status = "accepted"
            return ride
        
        @HF.safe_action_decorator
        def start_ride(self, ride_id: str):
            ride = self.ride_repo.get_ride(ride_id)
            if not ride:
                raise ValueError("Ride not found")
            elif ride.status != "accepted":
                raise ValueError("Ride not accepted yet")
            else:
                ride.status = "in_progress"
                return ride

        @HF.safe_action_decorator
        def complete_ride(self, ride_id: str):
            ride = self.ride_repo.get_ride(ride_id)
            if not ride:
                raise ValueError("Ride not found")
            elif ride.status != "in_progress":
                raise ValueError("Ride is not in progress")
            else:
                ride.status = "completed"
                return ride

        @HF.safe_action_decorator
        def cancel_ride(self, ride_id: str):
            ride = self.ride_repo.get_ride(ride_id)
            if not ride:
                raise ValueError("Ride not found")
            elif ride.status in ["completed", "cancelled"]:
                raise ValueError("Cannot cancel a completed or already cancelled ride")
            else:
                ride.status = "cancelled"
                return ride
        
        @HF.safe_action_decorator
        def view_ride(self, ride_id: str):
            ride = self.ride_repo.get_ride(ride_id)
            if not ride:
                raise ValueError("Ride not found")
            return ride
        
        @HF.safe_action_decorator
        def list_rides(self):
          return self.ride_repo.list_rides()
             