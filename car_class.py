class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometr = 14786

    def set_odometr(self, kilometr):
        if kilometr >= self.odometr:
            self.odometr = kilometr
        else:
            print("Скручиваем пробег?")

    def descriptio_name(self):
        long_name = f"{self.year} {self.make} {self.model} " \
                    f"пробег авто: {self.odometr}\n" \
                    f"{self.fill_gas()}"
        return long_name.title()

    def read_odometr(self):
        print(f"Пробег машины равен: {self.odometr}")

    def fill_gas(self):
        return f"Заправляем всегда АИ-95"

class Electrocar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    def describe_battery(self):
        print(f"Для машины {self.make.title()} батарея ")

    def fill_gas(self):
        return f"Это элетромобиль, бензин не нужен"

class Battery:

    def __init__(self, battery_size=99):
        self.battery_size = battery_size

    def descrip_battery(self):
        print(f"Размер батареи: {self.battery_size}")
