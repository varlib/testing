class User:
    def __init__(self, first_name, last_name, login, password, location):
        self.first_name = first_name
        self.last_name = last_name
        self.login = login
        self.password = password
        self.location = location

    def describe_user(self):
        print(f"Пользователь: {self.login} с паролем: {self.password}\n"
              f"Имя пользователя: {self.first_name} {self.last_name}\n"
              f"Местонахождения: {self.location}")

    def hello_user(self):
        print(f"Приветствую тебя: {self.first_name} {self.last_name}")
