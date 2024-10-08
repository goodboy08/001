class WashingMachine:
    h = 850
    w = 460
    c = 595
    brand = '海尔'

    def __init__(self):
        self.__color = 'red'

    def get_color(self):
        return '默认颜色为',self.__color
    
    def set_color(self,color):
        if color in ['red', 'blue', 'yellow']:
            self.__color = color
        else:
            print('违规的颜色')
    
    def start(self):
        print('启动洗衣机, 开始洗洗衣服')
    
    def stop(self):
        print('关闭洗衣机')

haier1 = WashingMachine()
haier1.set_color('pink')
print(haier1.get_color())