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

# built in functions

# absolute value
abs(-24)

# Bool condition none or zero = false
bool(None)

# dir gives all methods for entered value
# help gives info on methods
sent = "hello"
print(sent.islower())
help(sent.islower)


# eval takes in string and runs as python code, exec is the same as eval but with multiline code

sent2 = 'print("Hi")'
eval(sent2)

# str = string, float = ., int = number
a = 1
str(a)
# returns '1' as a string
float(a)
# returns 1.0 as a float
int(a)
# returns 1 as a number

# Classes


class Person:
    def getName(self):
        print("Zack")

    def getAge(self):
        print("25")


p = Person()

# Called like a function
p.getName()
p.getAge()

# init allows for extra parameters to be passed


class Person2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getThisName(self):
        print("Your name is " + self.name)

    def getThisAge(self):
        print("Your age is " + self.age)


p1 = Person2("Jeff", "40")
p1.getThisName()
p1.getThisAge()
