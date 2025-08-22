from Models.vehicles_model import Vehicle
from repositories.vehicle_repo import VehicleRepository
from utils.helper import HelperFunctions as HF

class VehicleService:
    def __init__(self, vehicle_repo : VehicleRepository):
        self.vehicle_repo = vehicle_repo

    @HF.safe_action_decorator
    def get_all_vehicles(self):
        return self.vehicle_repo.list_vehicles()

    @HF.safe_action_decorator
    def register_vehicle(self, driver_id, brand, model, year, plate_number,color):
        new_vehicle = Vehicle(driver_id, brand, model, year, plate_number, color)
        self.vehicle_repo.add_vehicle(new_vehicle)
        return new_vehicle
    
    @HF.safe_action_decorator
    def get_vehicle_by_id(self, vehicle_id):
        return self.vehicle_repo.get_vehicle(vehicle_id)
    
    @HF.safe_action_decorator
    def update_vehicle_info(self,vehicle_id, **kwargs):
        vehicle = self.vehicle_repo.get_vehicle(vehicle_id)
        if not vehicle:
            return None
        for key, value in kwargs.items():
            if hasattr(vehicle,key): setattr(vehicle,key,value)
        self.vehicle_repo.update_vehicle(vehicle)
        return vehicle