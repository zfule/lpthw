def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b

print("Let me do something!")
x = 110
my_height = add(100, 77)
my_weight = multiply(65, 1)

y = divide(subtract(my_height, x), my_weight)

print("Are you healthy?", y, "Sure?")

print("Other way:")

height = float(input("请输入身高（cm）： "))
weight = float(input("请输入体重（kg）： "))
y = divide(subtract(height, x), weight)

print("你健康吗？", y)
