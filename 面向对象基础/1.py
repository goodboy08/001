class Cat:
    def eat(self):
        print('小猫爱吃鱼')
    
    def drink(self):
        print('小猫家喝水')

tom = Cat()
tom.name = 'tom'

tom.drink()
tom.eat()
print(tom)
# print(f'{id(tom)}')

lazy_cat  = Cat()
lazy_cat.name = 'lazy'

lazy_cat.eat()
lazy_cat.drink()
print(lazy_cat)