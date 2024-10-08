class Animal:
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        print(self.name + " is eating.")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    
    def bark(self):
        print(self.name + " is barking.")

dog = Dog("Tom", "Husky")
dog.eat()  # 输出"Tom is eating."
dog.bark()  # 输出"Tom is barking."
