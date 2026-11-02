# question 01

def apply_to_all(numbers,action):
    result = []
    for n in numbers:
        result.append(action(n))
    return result
def double(n):
    return n * 2

print(apply_to_all([1, 2, 3], double))
print(apply_to_all([1, 2, 3], lambda n: n * n))
print(apply_to_all([1.6, 2.4], round))

# question 02

prices = [20, 75, 120, 45, 90]

above_50 =list(filter(lambda price: price > 50, prices))
add_10 = list(map(lambda price: price +10, above_50))

print(above_50)
print(add_10)

# question 03

words = ["banana", "fig", "cherry", "kiwi"]
students = [("Dana", 92), ("Avi", 78), ("Noa", 85)]
for name, grade in sorted(students, key=lambda x: x[1], reverse=True):
    print(name)

print(sorted(words, key=len))
print(max(words, key=len))

# question 04
def make_discount(percent):
    def discount(price):
        return price * (1 - percent / 100)
    return discount

ten_off = make_discount(10)
half_price = make_discount(50)
print(ten_off(200))
print(half_price(200))


# question 05

# def double(n):
#     return n * 2

# print(apply_to_all([1, 2], double())) אני לא מעביר שום דבר בתור ארגומנט בדאבל 

def apply_to_all(numbers, action):
    result = []
    for num in numbers:
        result.append(action(num))
    return result

def double(num):
    return num * 2


print(apply_to_all([1, 2], double))