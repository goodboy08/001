'''
python重写
在Python中，子类可以重写（覆盖）父类的方法，以实现自己的功能。
重写方法时，需要注意以下几点：

子类的方法名与父类的方法名相同。
子类的方法参数与父类的方法参数相同。
子类的方法返回值类型与父类的方法返回值类型相同或者是父类方法返回值类型的子类型。
'''
class Animal:
    def make_sound(self):
        print("The animal makes a sound.")

class Dog(Animal):
    def make_sound(self):
        print("The dog barks.")

my_dog = Dog()
my_dog.make_sound()  # 输出"The dog barks."