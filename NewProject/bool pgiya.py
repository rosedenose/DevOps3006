def remainder10(a):
    x = a % 10
    y = (a - x) / 10
    return (x, y)

s, r = remainder10(236)

print(s)
print(r)

while s != 0
    s, r = remainder10(s)
