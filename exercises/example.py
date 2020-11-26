"""An example illustrating a few aspects of inheritance"""


class Alice:

    def __init__(self, n):
        self.value = n

    def yell(self):
        return "Hei"

    def get_value(self):
        return self.value


class Bob(Alice):

    def __init__(self, n):
        Alice.__init__(self, n)

    def yell(self):
        return "Ho"


if __name__ == "__main__":
    a = Alice(4)
    b = Bob(3)

    a_list = [a, b]
    for p in a_list:
        print(p.yell(), p.get_value())
