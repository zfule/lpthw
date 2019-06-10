types_of_people = 10 #
x = f"There are {types_of_people} types of people." #对变量 x 赋值There are {types_of_people} types 0f people.

binary = "binary" #这里似乎没啥用，只是将字符串 binary 添了个变量名 binary
do_not = "don't" #同上。给 don't 加了个变量名 do_not
y = f"Those who know {binary} and those who {do_not}." #对变量 y 赋值 Those who know {binary} and those who {do_not}

print(x) #打印 x
print(y) #打印 y

print(f"I said : {x}") #打印 x 且前加 I said :
print(f"I also said : '{y}'") #打印 y ,且加 I also said : ''

hilarious = "True" #对变量 hilarious 赋值 True
joke_evaluation = "Isn't that joke so funny?! {}" #对变量 joke_evaluation 赋值 Isn't that joke so funny?!{}

print(joke_evaluation.format(hilarious)) #打印 joke_evaluation + hilarious

w = "This is the left side of..." #对 w 赋值 This is the left side of...
e = "a string with a right side." #对 e 赋值 a string with right side

print(w + e) #将变量 w 与 e 内的字符串拼接并打印出来
