def getSeries(a):
    arr = []
    if a%2==0:
        a = a-1
    for i in range(a):
        arr.append(2*i + 1)
    return arr

print(getSeries(1))
print(getSeries(2))
print(getSeries(3))
print(getSeries(4))
print(getSeries(5))