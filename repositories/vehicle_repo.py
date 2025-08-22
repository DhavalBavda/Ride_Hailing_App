class VehicleRepository:
    def __init__(self):
        self.vehicles = {}
    
    def add_vehicle(self,vehicle):
        self.vehicles[vehicle.id] = vehicle

    def get_vehicle(self,vehicle_id):
        return self.vehicles.get(vehicle_id)
    
    def update_vehicle(self,vehicle):
        if vehicle.id in self.vehicles:
            self.vehicles[vehicle.id] = vehicle
            return True
        return False
    
    def remove_vehicle(self,vehicle_id):
        if vehicle_id in self.vehicles:
            del self.vehicles[vehicle_id]
            return True
        return False