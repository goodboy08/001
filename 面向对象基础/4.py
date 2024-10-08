class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    def speak(self):
        return "Woof"

my_dog = Dog("Rufus")
print(my_dog.name)
print(my_dog.speak())
