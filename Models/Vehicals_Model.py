import time
import uuid

class Vehicle:
    def __init__(self, driver_id, brand, model, year, plate_number, color, vehicle_id=None):
        self.id = vehicle_id or str(uuid.uuid4())  # Auto-generate if not provided
        self.driver_id = driver_id
        self.brand = brand
        self.model = model
        self.year = year
        self.plate_number = plate_number
        self.color = color
        self.created_at = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    def __str__(self):
        return (f"Vehicle({self.id}, Driver: {self.driver_id}, {self.brand} {self.model}, "
                f"Year: {self.year}, Plate: {self.plate_number}, Color: {self.color}, "
                f"Created At: {self.created_at})")
