import numpy as np
list=np.random.randint(1,20,15)
print("Random vector before replacing max value ")
print(list)
result = np.where(list == np.amax(list))
n=result[0]
list[n] = 0
print("Random vector after replacing max value with zero")
print(list)




