#a = [4,6,2,3,6,7,55.4,9]
#a.sort(reverse=True)
#new_items = [item for item in a if int(item) == item]
#print (new_items)
#b=a[0:3]
#print(a)

"""b = [44,55,666777.55,33,1,2,4,6]
b.sort(reverse=True)
#print(b)
for i in b:
    #print(i)
    try:
        new_items = [item for item in b if int(item)]
        print(new_items)
    except:
        continue"""
import numpy as np
'''a = 5
zeros_array = np.zeros((a,a))
for i in zeros_array:
    x = 1
    x += zeros_array[i]
print(zeros_array'''
"""a = 4
array_1 = []
for i in range(a):
    array_1[i] = array_1[i] + i
print (array_1)"""

"""a = [4, 5555, 3, 2211.22, 3456, 443.33,'apple']
non_include = [x for x in a if not isinstance(x, int)]
"""for i in a:
    if str(i):
        non_include.append(i)"""
print(non_include)"""
