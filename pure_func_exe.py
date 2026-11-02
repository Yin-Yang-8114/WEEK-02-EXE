# question 01
"""
def square(n):  אין side effect
return n * n


def log_square(n):
print(&quot;squaring&quot;, n)                 print זה side effect? 
return n * n


def add_item(cart, item):
cart.append(item)                  אני משנה את הרשימה אז לא פונקציה טהורה
return cart


def with_item(cart, item):
return cart + [item]                                       pure because its creating an new list

""" 

# question 02 

def add_price(total,price):
    return total + price

total = 0
total = add_price(total, 10)
total = add_price(total, 10)
print(total)

print(add_price(0, 10))
print(add_price(0, 10))

# question 03

def apply_tax(price):
    tax = 1.17
    price_with_tax =[]
    for prud in price:
        price_with_tax.append(round((prud * tax),2))
    return price_with_tax
prices = [100, 50]
with_tax = apply_tax(prices)
print(prices)
print(with_tax)

#question 04

def calculate_total(prices):
    total =0 
    for price in prices:
        total += price
    return total

def show_total(total):
    print("total",calculate_total(total))
show_total([10, 20, 30])

# question 05

def top_three(numbers):
    num = sorted(numbers.copy(),reverse=True)
    return num[:3]

scores = [70, 95, 88, 60, 99]
print(top_three(scores))
print(scores)
