class Vehical:
    def __init__(self, name):
        self.name = name
    def started(self):
        print(f" {self.name} started ")
    def stopped(self):
        print(f"{self.name} stopped") 
class  car(Vehical):
    def sound(self):
        print(f"Hionk! Honk!")
my_car =  car("Toyota")
my_car.started()
my_car.sound()
my_car.stopped()


    


