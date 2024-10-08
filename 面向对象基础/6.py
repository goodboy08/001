class A:
    def method1(self):
        print("Method 1 of A called.")

class B:
    def method2(self):
        print("Method 2 of B called.")

class MyClass(A, B):
    def method3(self):
        print("Method 3 of MyClass called.")

my_object = MyClass()
my_object.method1()  # 输出"Method 1 of A called."
my_object.method2()  # 输出"Method 2 of B called."
my_object.method3()  # 输出"Method 3 of MyClass called."
