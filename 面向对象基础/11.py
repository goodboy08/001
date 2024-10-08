# 直接使用父类的类名调用父类的方法也是一种有效的方式。
class Animal:
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        print(self.name + " is eating.")

class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name)
        self.breed = breed
    
    def bark(self):
        print(self.name + " is barking.")

my_dog = Dog("Tom", "Husky")
my_dog.eat()  # 输出"Tom is eating."
