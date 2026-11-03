# question 01
def make_greeting(name, greeting="Hello", punct="!"):
    return f"{greeting}{name}{punct}"

print(make_greeting("Dana"))
print(make_greeting("Avi", "Good morning"))
print(make_greeting("Noa", punct="?"))

# question 02 
def average(*numbers):
    if len(numbers) == 0:
        raise ValueError("enter at least one number")
    return sum(numbers) / len(numbers)


print(average(80, 90))
print(average(70, 80, 90, 100))
try:
    average()
except ValueError as error:
    print("error:", error)

# question 03

def format_profile(name, **details):
    profile = f"Name: {name} "
    for key, value in details.items():
        profile += f"{key.capitalize()}: {value}"
    return profile  
print(format_profile("Dana", age=24, city="Haifa"))
print(format_profile("Avi"))


# question 04

products = [("Laptop", 3500), ("Mouse", 80), ("Desk", 900)]
for product in sorted(products, key=lambda x: x[1]):
    print(f"{product[0]}: {product[1]}")

print(f"the most expensive product {max(products, key=lambda x: x[1])[0]}")

# question 05

def add_item(item, cart=[]):
    cart.append(item)
    return cart

print(add_item("milk"))
print(add_item("bread"))

def add_item(item, cart=None):
    if cart is None:
        cart = []
    cart.append(item)
    return cart

print(add_item("milk"))
print(add_item("bread"))