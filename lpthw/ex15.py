from sys import argv

script, filename = argv #定义两个变量

txt = open(filename,encoding='UTF-8')

print(f"Here's your file {filename}:") #打印
print(txt.read()) #打印

print("Type the filename again:") #打印
file_again = input("> ") #定义

txt_again = open(file_again,encoding='UTF-8') #定义

print(txt_again.read()) #打印
