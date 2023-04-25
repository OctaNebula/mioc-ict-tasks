import re
a = input()
res = re.split("\s+", a)
while res.__contains__(''):
    res.remove('')
print(len(res))
