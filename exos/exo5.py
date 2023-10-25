
def calculateFactorialFromNumber(x):
    sum = 0
    for i in range(x):
        sum = sum * i+1
    return sum

print(calculateFactorialFromNumber(5))
