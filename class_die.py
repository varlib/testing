import random as rd


class Lottery:

    def __init__(self, list):
        self.list = list

    def get_win(self):
        n = 1
        win = []
        while n <= 4:
            result = rd.choice(self.list)
            win.append(result)
            n += 1
        return win
