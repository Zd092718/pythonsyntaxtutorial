print("Hello world")
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
