import re
a = input()
res = re.split("\s+", a)
while res.__contains__(''):
    res.remove('')
for i in res:
    if len(i) >= 5:
        print(i)
