# 使用super()函数调用父类的方法是比较常用的方式，
# 它可以自动识别出哪个父类的方法需要被调用。
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

my_dog = Dog("Tom", "Husky")
my_dog.eat()  # 输出"Tom is eating."