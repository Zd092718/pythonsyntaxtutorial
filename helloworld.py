# print to console
print("Hello world")

# variable declarations/ nice and easy
age = 15

# %d is an integer placeholder %s is a string placeholder
if(age > 25):
    print("You're getting old")
elif(age == 25):
    sent = "You are %d years old"
    print(sent % age)
else:
    sent = "You are %d years old wee child"
    print(sent % age)

# function defs


def HelloWorld():
    print("Hello World")


HelloWorld()


def Greeting(name):
    print("Hi " + name + "!")


Greeting("Zack")


def Sum(num1, num2):
    print(num1 + num2)


Sum(5, 40)


def returnSum(num1, num2):
    return (num1 + num2)


sum = returnSum(12, 23)

print(sum)
