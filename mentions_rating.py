import re

exampleFile = open(r'E:\html_pravda\texts\2021\dt\dt_headlines\dt_february.txt', encoding='utf-8') #txt file 
exampleFile1 = exampleFile.read()

name_1 = re.compile(r'Зеленськ') #name
head = name_1.findall(exampleFile1)
headli = ('\n'.join(head))
print(headli)
