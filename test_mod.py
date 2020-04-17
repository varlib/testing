class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Ресторан {self.restaurant_name}. Тип кухни: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"Наш ресторан {self.restaurant_name} сейчас открыт")
