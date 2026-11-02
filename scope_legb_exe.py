# question 01
# הוא נעלם ברגע שהפונקצייה מסתיימת כי הוא משתנה מקומי לפונקציה

def welcome(name):
    message = "welcome" +name
    return message

temp = welcome("chaim")
print(temp)
print(temp)

# question 02
"""
x = "global"

def first():
    x = "local in first" #local
    print("1:", x)

def second():
    print("2:", x) #global

first()
second()
print("3:", x) # global
"""

# question 03

# UnboundLocalError
count=0
def add_one(count):
    return count+1
count=add_one(count)
count=add_one(count)
print(count)


# question 04

# TypeError

list01= [1, 2, 3]
num=list(range(5))
print(list01, num)

# question 05
def add(price, cart, total):
    new_cart = cart + [price]
    final_total = total + price
    return new_cart, final_total


cart=[]
total =0

cart,total=add(100,cart,total)
cart,total=add(50,cart, total)

print(cart,total)