from sys import argv
from os.path import exists

script, from_file, to_file = argv

#一行代码：open(to_file,"w").write(open(from_file).read())
print(f"Copying from {from_file} to {to_file}")
#We could do these two on one line, how?
in_file = open(from_file, encoding='UTF-8') #打开文件并赋值给in_file
indate = in_file.read() #阅读in_file 文本内容并赋值给indate

print(f"The input file is {len(indate)} bytes long") #len(),返回文本长度
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w', encoding='UTF-8') #写入模式打开to_file并赋值给out_file
out_file.write(indate) #将变量indate内容写给out_file

print("Alriht, all done.")

out_file.close() #关闭文件
in_file.close() #关闭文件
