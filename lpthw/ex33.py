i = 0
numbers = []

while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i)

    i = i + 1
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")


print("The numbers:")

for num in numbers:
    print(num)

print("______________________")
# for & rnage
numbers = []
for i in range(0, 6):
    print(f"At the top i is {i}")
    numbers.append(i)
    print("Numbers now: ", numbers )
    print(f"At the bottom i is {i + 1}")

print("The numbers: ")

for num in numbers:
    print(num)
