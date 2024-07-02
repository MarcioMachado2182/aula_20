callables = []
a = ""
for i in (0, 1, 2, 3,4,5):
    a = i
    callables.append(lambda a=i: a)

for f in callables:
    print(f())