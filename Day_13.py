#LEARNING ABOUT CLASSES, OBJECTS, METHODS, ETC
class car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def describe(self):
        return f"{self.year} {self.make} {self.model}\n"
    
car1 = car('Toyota', 'Corolla', 2020)
car2 = car('Honda', 'Civic', 2019)    

# Access attributes and methods
print(car1.describe())  # Output: 2020 Toyota Corolla
print(car2.describe())  # Output: 2019 Honda Civic