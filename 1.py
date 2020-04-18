import class_die
import json

lotery_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'a', 's', 'd', 'f', 'g']
lott = class_die.Lottery(lotery_list)
numbers = lott.get_win()
print(numbers)

filename = '../files/test.json'
with open(filename, 'a') as f:
    json.dump(numbers, f)
