# """

# Description :- the code for polymorphism example 1
# Author :- Sarthak Modi

# """
# class  Vehicle:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#         def move(self):
#             print("Move!")
# class Car(Vehicle):
#     pass
# class Boat(Vehicle):
#     def move(self):
#         print("Sail!")
# class Plane(Vehicle):
#     def move(self):
#         print("Fly!")
# car1 = Car("Ford", "Mustang") 
# boat1 = Boat("Ibiza", "Touring 20") 
# plane1 = Plane("Boeing", "747") 
# for x in (car1, boat1, plane1):
#   print(x.brand)
#   print(x.model)
#   x.move()


"""

Description :- the code for polymorphism example 2
Author :- Sarthak Modi

"""

class Device :
    def turn_on(self):
        pass
class TV(Device):
    def turn_on(self):
        return " TV is ON now"
class Fan(Device):
    def turn_on(self):
        return "Fan is spinning now"
class Light(Device):
    def turn_on(self):
        return "Light is On Now"
def active_device(Device):
    print(Device.turn_on())
tv = TV()
fan = Fan()
light = Light()
active_device(tv)
active_device(fan)
active_device(light)

