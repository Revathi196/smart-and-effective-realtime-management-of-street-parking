class Vehicle:
    def __init__(self, plate_number, brand, model):
        self.plate_number = plate_number
        self.brand = brand
        self.model = model

    def __str__(self):
        return f"{self.brand} {self.model} (Plate: {self.plate_number})"
