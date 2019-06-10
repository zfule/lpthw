from textwrap import dedent

x = 'family'
print(dedent("""{}:
father
and
mother
I love you """.format(x)))

print("Mary had a little lamb.") #打印字符串
print("Its fleece was white as {}.".format('snow')) #打印字符串及{}内字符串
print("And everywhere that Mary went.") #打印字符串
print("." * 10) #打印10个 .

end1 = "C" #定义变量
end2 = "h" #定义变量
end3 = "e" #定义变量
end4 = "e" #定义变量
end5 = "s" #定义变量
end6 = "e" #定义变量
end7 = "B" #定义变量
end8 = "u" #定义变量
end9 = "r" #定义变量
end10 = "g" #定义变量
end11 = "e" #定义变量
end12 = "r" #定义变量

# watch that comma at the end. try removing it to see what happens
print(end1 + end2 + end3 + end4 + end5 + end6, end = ' ')
print(end7 + end8 + end9 + end10 + end11 + end12)



print(end1)
print(end2)
print(end3)
print(end4)
print(end5)
print(end1 + end2)
print(end1 + end2, end=' ')
print(end3 + end4 + end5)

print(end3 + end4, end=' ')
print(end5)
