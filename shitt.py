import pandas as pd 
l1 = [1,"A",21]
s1 = pd.Series(data = l1*2)
print(s1)


s1 = pd.Series([1,7,21])
print(s1)

import numpy as num 
arr = num.array([1,7,21])
s1 = pd.Series(arr,index=(7,77,777))
print(s1)

arr = num.array([31,47,121])
s1 = pd.Series(arr,index=(7,77,777))
print(s1[777])
 
l1 = list("My name is ravi")
s1 = pd.Series(l1)
print(s1[0])   