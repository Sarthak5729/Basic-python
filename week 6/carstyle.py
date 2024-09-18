class car:
    def  __init__(self, color, model, year):
        self.color = color
        self.model =model
        self.year = year
    def drive(self):
        print(f"the {self.color} {self.model} build in {self.year} is driving")

    def  stop(self):
        print(f"the {self.color} {self.model} build in {self.year} is stopped")
car1 = car("Red" , "Toyota " , 2020)
car2 = car("Black" , "BMW" ,  2019)

car1.drive()
car1.stop()
car2.drive()
car2.stop()