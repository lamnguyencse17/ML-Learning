import numpy as np

#init
arr = np.array([0, 0.1, 2])


#reference
arr2 = arr

#copy
arr3 = arr.copy()

#casting
arr4 = arr.astype(np.float32)

#NaN no integer
nanArr = np.array([np.nan, 'abc'])

#infinity no integer
infArr = np.array([np.inf, 5])

#Time to code section
firstArr = np.array([np.nan, 2,3,4,5])
secondArr = firstArr.copy()
secondArr[0]=10
float_arr = np.array([1,5.4,3])
float_arr2 = secondArr.astype(np.float32)
matrix = np.array([[1,2,3],[4,5,6]], dtype=np.float32)

