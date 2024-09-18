class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f" {self.name} makes sound ")
class dog(Animal):
    def bark(self):
        print(f"{self.name} bark!")
my_dog = dog("Buddy")
my_dog.speak()
my_dog.bark()

