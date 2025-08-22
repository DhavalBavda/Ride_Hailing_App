from Models.rides_model import RidesModel
from repositories.ride_repo import RideRepository
from repositories.user_repo import UserRepository
from repositories.vehicle_repo import VehicleRepository
import uuid 

class RideService:
        def __init__(self, ride_repo: RideRepository, user_repo: UserRepository, vehicle_repo: VehicleRepository):
            self.ride_repo = ride_repo
            self.user_repo = user_repo
            self.vehicle_repo = vehicle_repo

        def request_ride(self, rider_id: str, driver_id: str, pickup: str, drop: str):
            rider = self.user_repo.get_user(rider_id)
            driver = self.user_repo.get_user(driver_id)
            if not rider or not driver:
                raise ValueError("Invalid rider or driver")
            ride = RidesModel(str(uuid.uuid4()), rider, driver, pickup, drop, status="requested")
            self.ride_repo.add_ride(ride)
            return ride
        

        def start_ride(self, ride_id: str):
            ride = self.ride_repo.get_ride(ride_id)
            ride.status = "in_progress"
            return ride

        def complete_ride(self, ride_id: str):
            ride = self.ride_repo.get_ride(ride_id)
            ride.status = "completed"
            return ride

        def cancel_ride(self, ride_id: str):
            ride = self.ride_repo.get_ride(ride_id)
            ride.status = "cancelled"
            return ride
        
        def view_ride(self, ride_id: str):
            ride = self.ride_repo.get_ride(ride_id)
            if not ride:
                raise ValueError("Ride not found")
            return ride
             