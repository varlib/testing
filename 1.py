from test_mod import *
from user_class import *
from car_class import *

# restaurant = Restaurant("Голубая лагуна", "Русская")
# restaurant1 = Restaurant("МореМания", "Итальянская")
# restaurant2 = Restaurant("Якитория", "Китайская")
#
# restaurant.describe_restaurant()
# restaurant1.describe_restaurant()
# restaurant2.describe_restaurant()
#
# user1 = User("Иванов", "Иван", "ivanov", "123", "Иваново")
# user2 = User("Петров", "Василий", "admin", "qwerty", "Махачкала")
#
# user2.hello_user()
# user2.describe_user()
# user1.hello_user()

# car_title = Car(year="2020", make="kia", model="sorento")
# car_title.set_odometr(14785)
# print(car_title.descriptio_name())
# car_title.read_odometr()
#
# restaurant.set_number_served(15)
# restaurant.open_restaurant()
# restaurant.increment_served(7)
# restaurant.open_restaurant()

electro_car = Electrocar("tesla", "model s", 2020)
print(electro_car.descriptio_name())
electro_car.battery.descrip_battery()