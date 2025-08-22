import time
import uuid  

class RidesModel:
    def __init__(self, rider_id, driver_id, pickup, drop_location, status, fare):
        self.id = str(uuid.uuid4())  
        self.rider_id = rider_id
        self.driver_id = driver_id
        self.pickup = pickup
        self.drop = drop_location
        self.status = status
        self.fare = fare
        self.created_at = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    def __str__(self):
        return (f"Ride({self.id}, Rider: {self.rider_id}, Driver: {self.driver_id}, "
                f"Pickup: {self.pickup}, Drop: {self.drop}, Status: {self.status}, Fare: {self.fare} "
                f"Created At: {self.created_at})")
