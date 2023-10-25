def filterByInsertion(values):
    for i in range(1, len(values)):
        j = i
        while j > 0 and values[j-1] > values[j]:
            values[j-1], values[j] = values[j], values[j-1]
            j -= 1
    return values

import random

result = [random.randint(1, 100) for _ in range(8)]
filterByInsertion(result) 
print ("Du plus petit au plus grand :")
for i in range(len(result)): 
    print ("% d" % result[i])
