from random import randint

class Person:
    name = 'Вячеслав'
    email = f'slavik_eremin_22_777@yandex.ru'
    password = f'12345678'
    password_bad = f'12345'

class RandomData:
    name = 'Вячеслав'
    email = f'slavik_eremin_22_{randint(0, 999)}@yandex.ru'
    password = f'123{randint(10000, 99999)}qwe'

class ConstructionModuleData:
    Bun = 'Булки'
    Sauce = 'Соусы'
    Filling = 'Начинки'