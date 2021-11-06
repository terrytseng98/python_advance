import numpy as np

listA=[4,3,8,3,9,10,2,7]
index=np.argsort(listA)

print(index)
print(np.array(listA)[index])