class Animal:
    def __init__(self, name, weight, speed):
        self.name = name
        self.weight = weight
        self.speed = speed

    def run(self):
        print(f'Я бегаю со скоростью {self.speed}')

my_animal = Animal('Sobaka', 7, 10)

print(my_animal.name)
print(my_animal.weight)
my_animal.run()
