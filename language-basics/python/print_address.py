an_object = {"a": 1}
object_id = id(an_object)

print(object_id)
print(hex(object_id))

# String Immutability
s = "abc"
s1 = s
print('address of s: ', id(s))

s = s + "def"
print('address of s, after concatenation: ', id(s))
print('address of s1: ', id(s1))

# Address of n also changed (?) - are they also immutable in python
n = 24
print('address of n: ', id(n))
n = n + 100
print('address of n, after modification: ', id(n))
