from test_mod import *
from user_class import *

restaurant = Restaurant("Голубая лагуна", "Русская")
restaurant1 = Restaurant("МореМания", "Итальянская")
restaurant2 = Restaurant("Якитория", "Китайская")

restaurant.describe_restaurant()
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()

user1 = User("Иванов", "Иван", "ivanov", "123", "Иваново")
user2 = User("Петров", "Василий", "admin", "qwerty", "Махачкала")

user2.hello_user()
user2.describe_user()
user1.hello_user()