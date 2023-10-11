class Animal:
    def make_noise(self):
        pass

class Dog(Animal):
    def make_noise(self):
        print('Arf-arf-arf')

class Cat(Animal):
    def make_noise(self):
        print('Meow-meow-meow')

my_dog = Dog()
my_cat = Cat()

my_dog.make_noise()
my_cat.make_noise()
