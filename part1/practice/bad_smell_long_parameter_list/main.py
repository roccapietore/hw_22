# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)


class Unit:
    def __init__(self, field):
        self.speed = 1
        self.field = field

    def speed(self, movement):
        if movement == "fly":
            return self.speed * 1.2
        elif movement == "crawl":
            return self.speed * 0.5

    def move_unit(self, direction, x, y):
        speed = self.speed()

        if direction == 'UP':
            coord = (x, y + speed)
        elif direction == 'DOWN':
            coord = (x, y - speed)
        elif direction == 'LEFT':
            coord = (x - speed, y)
        elif direction == 'RIGTH':
            coord = (x + speed, y)

        return self.field.set_unit(coord, unit=self)

