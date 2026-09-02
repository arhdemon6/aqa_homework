class Rhombus:

    def __init__(self, side_a, angle_a):
        self.side_a = side_a
        self.angle_a = angle_a

    def __setattr__(self, name, value):
        if name == 'side_a':
            if value <= 0:
                raise ValueError('Сторона повинна бути більше 0')
            super().__setattr__(name, value)

        elif name == 'angle_a':
            if not (0 < value < 180):
                raise ValueError('Кут повинен бути в межах від 0 до 180')
            super().__setattr__(name, value)
            super().__setattr__('angle_b', 180 - value)
        else:
            super().__setattr__(name, value)

    def show_info(self):
        print(f'Сторона a: {self.side_a}')
        print(f'Кут a: {self.angle_a}°')
        print(f'Кут b: {self.angle_b}°')

side_a_input = float(input('Введіть довжину сторони a: '))
angle_a_input = float(input('Введіть кут a (0-180): '))

rhombus1 = Rhombus(side_a_input, angle_a_input)
rhombus1.show_info()