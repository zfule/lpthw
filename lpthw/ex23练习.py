from sys import argv

script, filename = argv


languages = open(filename, encoding='UTF-8')
print(languages.read())
