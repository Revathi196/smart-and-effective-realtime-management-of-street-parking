from parking_manager import ParkingManager
from vehicle import Vehicle

def main():
    manager = ParkingManager()
    
    # Adding vehicles to parking spots
    manager.park_vehicle(Vehicle("ABC123", "Toyota", "Camry"))
    manager.park_vehicle(Vehicle("XYZ789", "Honda", "Civic"))
    
    # Listing parked vehicles
    print("Parked Vehicles:")
    for vehicle in manager.get_all_vehicles():
        print(vehicle)
    
    # Removing a vehicle
    manager.remove_vehicle("ABC123")
    print("\nUpdated Parking List:")
    for vehicle in manager.get_all_vehicles():
        print(vehicle)
    
if __name__ == "__main__":
    main()
