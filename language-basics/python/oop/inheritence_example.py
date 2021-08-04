from person import Person

"""
NOTE:
    - use the 'pass' keyword you want to do nothing in a method, function or in a class and don't want to get an error
    message from the compiler.
"""


def do_nothing():
    pass


class EmptyClass:
    pass


"""
Creating subclass from Person class.
It will get everything a Person class has
"""


class OldPerson(Person):
    pass


op = OldPerson('Asif', 'Ahmed', 'M', '68')
print(op)  # Asif Ahmed, 68, M
print(op.full_name)

"""
Creating 'Student' subclass from 'Person' class
We can do several things in the subclass 'Student':
    - adding new attribute
    - overriding the constructor __init__
    - modifying existing person method (see __str()__ method modified) 
    - adding new method (see registration() method)
"""


class Student(Person):
    # Adding attribute using class property
    university_code = "JU"

    # Adding new attribute through __init__ method
    # Person.__init__() and super().__init__ could be used interchangeably
    def __init__(self, fn, ln, sx, ag, bth, dpt):
        # Person.__init__(self, fn, ln, sx, ag)
        super().__init__(fn, ln, sx, ag)
        self.batch = bth
        self.department = dpt

    # Modifying existing method
    # Note how the super class version is called
    def read(self):
        super().read()
        print(self.full_name + ' reading text book for exam ....')

    # Modifying existing method and using super() keyword
    # Note, how the __st()__ method is called from child class  - super(Student, self)._str()__  'self' is not at first
    def __str__(self):
        return super(Student, self).__str__() + ', batch: ' + str(self.batch) + ', department: ' + self.department

    # Adding new method
    def enroll(self):
        print(self.full_name + ' enrolling for a subject ...')


s1 = Student(fn='Nazmul', ln='Hassan', sx='M', ag=20, bth=48, dpt='CSE')
print(s1)  # Nazmul Hassan, 20, M, batch: 48, department: CSE
s1.read()  # Nazmul Hassan reading text book for exam ....
s1.enroll()  # Nazmul Hassan enrolling for a subject ...
