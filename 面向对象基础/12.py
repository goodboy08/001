'''
在Python中，super()函数用于调用父类的方法。使用super()函数调用父类的方法时，

可以不使用父类的类名，而是使用super()函数自动识别出需要调用的父类的方法。

super()函数的语法如下：

super([type[, object-or-type]])

其中，type是子类的类型，object-or-type是子类的对象或类型。如果只有一个参数，则默认为子类的类型。

'''

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