def myFunction1():
    print("Hello, world!")

def myFunction2(fname, lname):
    print(fname + " " + lname) # menggunakan parameter

def myFunction3(*kids):
    print("The yooungest child is " + kids[2]) # pilih berdasarkan array & args

def myFunction4(child1, child2, child3):
    print("The Youngest Chlid is " + child3) # pilih berdasarkan parameter

def myFunction5(**kids):
    print("His last name is " + kids["lname"] + " and " + kids["fname"]) # Tes dengan parameter yang ada di function main

def myFunction6(country = "Norway"):
    print("I am from " + country)

def myFunction7(food):  # auto print dengan for dan in
    for x in food:
        print(x)

def myFunction8(x):         #tes kalkulasi sederhana
    return print (5 * x)

def myFunction9(x, /):      # tes running
    print(x)

def myFunction10(x):        # tes input value di main
    print(x)

def recursion(x):
    if (x > 0 ) :
        result = x + recursion(x - 1)
        print(result)
    else:
        result = 0
    return result


fruits = ["apple", "orange", "melon"]


# myFunction1()
# myFunction2("emil", "bagus")
# myFunction3("Emil", "Tobisa", "Hehe")
# myFunction4(child1 = "Jonathan", child2 = "Dasthin", child3 = "Bagus")
# myFunction5(fname = "tobias", lname = "dasthin")
# myFunction6("Indonesian")
# myFunction6("Malaysian")
# myFunction7(fruits)
# myFunction8(8)
# myFunction9(10)
# myFunction10(x = 10)
print("return recursion results ")
recursion(10)