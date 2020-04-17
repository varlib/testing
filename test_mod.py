def hello(names='', txt="Привет дружок"):
    print(f"{txt} {names.title()}")


def is_num(num):
    if num.isdigit():
        return "Это число"
    else:
        try:
            float(num)
            return "Это число"
        except ValueError:
            return "Это нифига не число"
