class car:
    def  __init__(self, color, model, year):
        self.color = color
        self.model = model
        self.year = year
    def drive(self):
        print(f"The {self.color} {self.model} is Driving")
    def stop(self):
        print(f"The {self.color} {self.model} has stopped")
    def display_info(self):
        print(f"Color: {self.color}, Model: {self.model}, Year: {self.year}")
class Electrioccar(car):
    def __init__(self, color, model, year, battery_capacity):
        super().__init__(color, model, year)
        self.battery_capacity = battery_capacity
    def display_info(self):
        super().display_info()
        print(f"Battery capacity : {self.battery_capacity} KWH")
my_electric_car =  Electrioccar("Blue", "Tesla", 2020, 102)
my_electric_car.drive()
my_electric_car.stop()
my_electric_car.display_info()

