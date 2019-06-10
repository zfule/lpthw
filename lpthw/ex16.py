from sys import argv

script, filename = argv

print(f"We are going to erase {filename}.") #打印
print("If you don't want that, hit CTRL-C (^C).") #打印
print("If you do want that, hit RETURN.") #打印

input("?")

print("Opening the file...")
target = open(filename, 'w') #写入模式打开

print("Truncating the file.  Goodbye!")
target.truncate() #清空文本

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

#一行代码：target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
target.close()
