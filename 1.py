from test_mod import *

active = True

while active:
    name = input("Введите ваше имя: ")
    if name == 'quit':
        hello(txt='Всем спасибо, все свободны!')
        active = False
    else:
        hello(names=name)
        is_nums = is_num(name)
        print(is_nums)
