# Тема 10. Декораторы и исключения
Отчет по Теме #10 выполнил(а):

- Черезов Роман Алексеевич
ЗПИЭ-20-1

| Задание   | Сам_раб |
|-----------|---------|
| Задание 1 | +       |
| Задание 2 | +       |
| Задание 3 | +       |
| Задание 4 | +       |
| Задание 5 | +       |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.

## Самостоятельная работа №1
### Самостоятельно создайте класс и его объект. Они должны отличаться, от тех, что указаны в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.
```python
class Animal:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

my_animal = Animal('Sobaka', 7)

print(my_animal.name)
print(my_animal.weight)
```
## Результат.
![Tema8_1](https://github.com/DarknessWillCame/TEMA-8/assets/46960566/69feba62-13df-4ac2-94ff-3f2e470555e3)

Результат задания 1

## Выводы
Я узнал, что в Python можно создавать классы и тем самым использовать парадигму ООП

## Самостоятельная работа №2
### Самостоятельно создайте атрибуты и методы для ранее созданного класса. Они должны отличаться, от тех, что указаны в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.
```python
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
```
## Результат.
![Tema8_2](https://github.com/DarknessWillCame/TEMA-8/assets/46960566/cc7a82e5-6210-4edb-b470-83749fc7e32b)

Результат задания 2

## Выводы
Я узнал, как для класса добавить аттрибуты speed и run(), которые выводят в консоль сообщение и сообщают о скорости передвижении

## Самостоятельная работа №3
### Самостоятельно реализуйте наследование, продолжая работать с ранее созданным классом. Оно должно отличаться, от того, что указано в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.
```python
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
```
## Результат.
![Tema8_3](https://github.com/DarknessWillCame/TEMA-8/assets/46960566/7351def7-7960-4ca5-ac1d-a13fb8a8fbce)

Результат задания 3

## Выводы
Наследование является мощным инструментом в ООП для переиспользования и композиции кода

## Самостоятельная работа №4
### Самостоятельно реализуйте инкапсуляцию, продолжая работать с ранее созданным классом. Она должна отличаться, от того, что указана в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.
```python
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
```
## Результат.
![Tema8_4](https://github.com/DarknessWillCame/TEMA-8/assets/46960566/74b83436-cb84-436d-83cd-a4e281985879)

Результат задания 4

## Выводы
Инкапсуляция позволяет ограничить доступ к некоторым аттрибутам класса

## Самостоятельная работа №5
### Самостоятельно реализуйте полиморфизм. Он должен отличаться, от того, что указан в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.
```python
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
```
## Результат.
![Tema8_5](https://github.com/DarknessWillCame/TEMA-8/assets/46960566/9563eb4b-366a-421c-bee1-638c686f111a)

Результат задания 5

## Выводы
Благодаря полиморфизму для разных классов у нас есть общий интерфейс

## Общие выводы по теме
Выполнив задание я узнал, что Python поддерживает классы, что позволяет писать код в парадигме ООП
