class ParkingManager:
    def __init__(self):
        self.vehicles = {}

    def park_vehicle(self, vehicle):
        if vehicle.plate_number not in self.vehicles:
            self.vehicles[vehicle.plate_number] = vehicle
        else:
            print("Vehicle is already parked.")

    def get_all_vehicles(self):
        return self.vehicles.values()

    def remove_vehicle(self, plate_number):
        if plate_number in self.vehicles:
            del self.vehicles[plate_number]
        else:
            print("Vehicle not found.")
