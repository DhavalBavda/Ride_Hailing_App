class RideRepository:
    def __init__(self):
        self.rides = {}

    def add_ride(self,ride):
        self.rides[ride.id] = ride
    
    def get_ride(self,ride_id):
        return self.rides[ride_id]