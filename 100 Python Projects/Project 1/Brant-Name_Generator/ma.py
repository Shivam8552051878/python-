"""
import time
val = "Slippper"
print(
    val[::-1]
)
print(time.time())


a = [1,2,3]
b = [3,4,5]
print(set(a) - set(b), set(b) - set(a))
c = a.copy()
c[1] = "duo"
print(a)
txt = "Hello World"
print(txt[2:5])

age = 36
txt = "My name is John, and I am {}"

print(txt.format(age))
print(bool("abc"))"""

import numpy as np

arr1 = [[1,2,3],[1,2,3]]
arr2 = [[4,5,6],[4,5,6]]

np_arr1 = np.array(arr1)
np_arr2 = np.array(arr2)


arr3 = []
for i in range(0,len(arr1)):
    arr4 = []
    for j in range(0,len(arr1[0])):
        arr4.append(arr1[i][j] * arr2[i][j])
    arr3.append(arr4)
    
print(arr3)
        
print(np.multiply(np_arr1 , np_arr2))