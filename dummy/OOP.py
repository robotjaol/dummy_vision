# --- Simple Class yang mungkin tidak dipakai ----
# class myClass :
#     x = 5

# p1 = myClass()
# print(p1.x)

# Simple Class dengan function
# class person :
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# val = person("Any", 20)

# print(val.name)
# print(val.age)

# basic
# class person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     # def __str__(self):
#         # return f"{self.name}({self.age})"

#     def myFunc(self):
#         print("hello my name is " + self.name)

# p1 = person("Jonathan", 10)
# p1.myFunc()

# using another named of self

class person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age

    def myFunc(abc):
        print("Hello my name is " + abc.name)

add = person("Jonathan", 20)
add.myFunc()

