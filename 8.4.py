class Animal:
    def __init__(self, name, weight, speed):
        self.name = name
        self.weight = weight
        self.speed = speed
    def run(self):
        print(f'Я бегаю со скоростью {self.speed}')

class Dog(Animal):
    def __init__(self, name, weight, speed, tail_length):
        super().__init__(name, weight, speed)
        self.__tail_length = tail_length
    def arf(self):
        print('Arf-arf')
    def wag_tail(self):
        print(f'Хвост размером {self.__tail_length}')

my_dog = Dog('Sobaka', 7, 10, 5)
# print(my_dog.__tail_length) защищённый аттрибут
my_dog.wag_tail()
