class VehicleRepository:
    def __init__(self):
        self.vehicles = {}
    
    def add_vehicle(self,vehicle):
        self.vehicles[vehicle.id] = vehicle

    def get_vehicle(self,vehicle_id):
        return self.vehicles.get(vehicle_id)
    
    def list_vehicles(self):
        return list(self.vehicles.values())