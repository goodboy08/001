# 方法重写：方法重写是指在子类中重新定义父类的方法，
# 从而实现对该方法的重载。这种方式可以让子类对父类的方法进行扩展或修改，
# 从而实现多态。
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("汪汪汪！")

class Cat(Animal):
    def speak(self):
        print("喵喵喵！")