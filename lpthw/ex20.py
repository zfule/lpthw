from sys import argv

script, input_file = argv

#创建函数——打印所有内容
def print_all(f):
    print(f.read())

#创建函数——回到第一行
def rewind(f):
    f.seek(0)

#创建函数——打印行数与一行文本内容
def print_a_line(line_count, f):
    print(line_count, f.readline(), end='')

current_file = open(input_file)

print("First let's print the whole file: \n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
