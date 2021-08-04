from person import Person

p1 = Person('Nazmul', 'Hasan', 'M', 20)
p2 = Person('Neyamul', 'Hasan', 'M', 18)
print(p1)
print(p2)

p1.occupation = 'Student'
print(p1.occupation)
print(dir(p1))
# print(p2.occupation)  # AttributeError - cause p2 has no attribute named 'occupation'

del p1.occupation
del p1.full_name
# print(p1.occupation)  # AttributeError
# print(p1.full_name)  # AttributeError
print(p2.age)  # 18

"""
NOTE:
    - you can add attribute in python object even if the class definition doesn't contain that attribute.
    We have added attribute 'occupation' to p1 even though the Person class doesn't have it.
    - 'del' keyword not only remove the value of attribute it delete the attribute itself.
"""