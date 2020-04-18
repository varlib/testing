class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Ресторан {self.restaurant_name}. Тип кухни: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"Наш ресторан {self.restaurant_name} сейчас открыт.\n"
              f"Обслужено посетителей {self.number_served}")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_served(self, number):
        self.number_served += number
