from repositories.ride_repo import RideRepository
from repositories.user_repo import UserRepository
from repositories.vehicle_repo import VehicleRepository

def main():

    # Initialize Repositories
    user_repo = UserRepository()
    vehicle_repo = VehicleRepository()
    ride_repo = RideRepository()