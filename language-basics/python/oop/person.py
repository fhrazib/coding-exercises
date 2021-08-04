class Person:
    alive = True

    def __init__(self, fn, ln, sx, ag):
        self.first_name = fn
        self.last_name = ln
        self.sex = sx
        self.age = ag
        self.full_name = self.first_name + " " + self.last_name

    def __str__(self):
        return self.full_name + ", " + str(self.age) + ", " + self.sex

    def read(self):
        print(self.full_name + ' reading news papers....')
