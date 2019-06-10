people = 30
cars = 40
trucks = 15


if cars > people:#判断车数是否大于人数，如果真，则打印下面内容；如果假执行下一条语句
    print("We should take the cars.")
elif cars < people:#判断车数是否小于，如果真，打印下面内容；如果假执行下一条语句
    print("We should not take the cars.")
else:
    print("We can't decide.")

if  trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we should take the trucks.")
else:
    print("We still can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")

if cars > people and people > trucks:
    print("We need {} trucks.".format(people / 2 - trucks))
