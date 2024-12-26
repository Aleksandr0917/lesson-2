import threading
from time import sleep


class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.enemies = 100  # Общее количество врагов
        self.days = 0  # Счетчик дней

    def run(self):
        print(f"{self.name}, на нас напали!")

        while self.enemies > 0:
            sleep(1)  # Пауза в 1 секунду, чтобы симулировать день сражения
            self.days += 1
            self.enemies -= self.power

            # Обработка количества оставшихся врагов
            if self.enemies < 0:
                self.enemies = 0

            day_word = "день" if self.days == 1 else "дня"
            print(f"{self.name}, сражается {self.days} {day_word}..., осталось {self.enemies} воинов.")

        print(f"{self.name} одержал победу спустя {self.days} {day_word}!")


# Создание рыцарей
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

# Запуск потоков
first_knight.start()
second_knight.start()

# Ожидание завершения потоков
first_knight.join()
second_knight.join()

# Вывод строки об окончании битв
print("Все битвы закончились!")

