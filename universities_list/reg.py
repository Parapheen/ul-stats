with open('unis.txt', 'r') as f:
    s = [line.strip().replace('\\n', '\n') for line in f]        
    data = ''.join(s)


import re


reg = r'\'(.*?)\['

with open('unis.txt', 'a') as f:
    l = re.findall(reg,data)
    for i in l:
        i = re.sub(r'[",\'\[\]]', '', i)
        print(i, file=f)