name = "zhanglele"
age = 10
fun = "{}"
w = "This is the left side of..." #对 w 赋值
e = "a string with a right side." #对 e 赋值

print(f"My name is {name}.")
print("I am ", age, "years old.")
print("I am {} years old.".format(age))
print("I am {} years old.".format('10'))
print(fun.format(f'My name is {name}.'))
print(w, end=' ')
print(e)
