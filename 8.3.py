class Animal:
    def __init__(self, name, weight, speed):
        self.name = name
        self.weight = weight
        self.speed = speed
    def run(self):
        print(f'Я бегаю со скоростью {self.speed}')

class Dog(Animal):
    def __init__(self, name, weight, speed):
        super().__init__(name, weight, speed)
    def arf(self):
        print('Arf-arf')

my_dog = Dog('Sobaka', 7, 10)
print(my_dog.name)
print(my_dog.weight)
my_dog.arf()
