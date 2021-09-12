s = input()
upper = 0
lower = 0
for i in s:
    if i.isupper():
        upper = upper + 1
    if i.islower():
        lower = lower + 1
if upper > lower:
    print(s.upper())
else:
    print(s.lower())