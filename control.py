# 1. Класс автобус.
class Autobus:
    def __init__ (self, speed, capacity, maxSpeed, passengers_names, hasEmptySeats, passengers):
        self.speed = speed
        self.capacity = capacity
        self.passengers = passengers
        self.hasEmptySeats = hasEmptySeats
        self.maxSpeed = maxSpeed
        self.passengers_names = passengers_names
#Функция, которая "создает" пассажиров.
    def add_passenger(self, passengers_names):
        persons_places = [i for i in range(1, 2)]
        persons_names = [input() for _ in range(1, 2)]
        self.passengers_names = dict(zip(persons_places, persons_names))
        print('Введите имя пассажира, которого вы хотели бы добавить:')
        new_name = input()
        if new_name in self.passengers_names:
            print('Он уже существует!')
        else:
            self.passengers_names['3'] = new_name
#создаем функцию, которая отвечает за высадку пассажиров.
    def get_que_passengers(self, passengers, hasEmptySeats):
        print('Сколько пассажиров высадить?')
        gets_passengers = int(input())
        if gets_passengers > self.passengers:
            print('Ошибка!')
            self.hasEmptySeats = True
        else:
            self.passengers -= gets_passengers
#создаем функцию, которая может еще добавить пассажиров
    def set_passengers(self, passengers, capacity):
        print('Взять попутчиков?')
        print('Да или нет:')
        choice = str(input())
        if choice.lower() == 'да':
            print('Сколько нужно добавить пассажиров?')
            que_new = int(input())
            if  self.capacity - self.passengers == 0:
                print('Мест нет!')
                self.hasEmptySeats = False
            else:
                self.passengers += que_new
                self.hasEmptySeats = True
        else:
            print('Поездка продолжается')
#Функция, позволяющая поднимать уровень скорости автобуса.
    def add_speed(self, speed):
        if self.speed == self.maxSpeed:
            print('Maximum')
        else:
            print('Поднять уровень скорости до:')
            new_speed = int(input())
            if self.speed + new_speed <= self.maxSpeed:
                self.speed += new_speed
            else:
                print('Невозможно!')
#Функция, позволяющая сбрасывать скорость.
    def distr_speed(self, speed):
        print('На сколько сбросить скорость?')
        district = int(input())
        self.speed -= district
        if self.speed < 0:
            print('Начните движение, пассажиры ждут')
            self.speed += 1

    def main(self):
        auto_bus = Autobus(9, 134, 2456, 130),
        auto_bus.add_passenger(),
        auto_bus.distr_speed(),
        auto_bus.set_passengers(),
        auto_bus.get_que_passengers(),
        auto_bus.add_speed(),
        print(bus.speed)

        main()








