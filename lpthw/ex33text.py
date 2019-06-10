def print_while(*c):


    i = 0
    numbers = []

    while i < q:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + x
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")


    print("The numbers: ")

    for num in numbers:
        print(num)


print("""这是一个循环程序。
你可以选择循环终点，以及跳跃数。""")

q = int(input("请输入循环终点："))
x = int(input("请输入跳跃数："))

print_while(q, x)
