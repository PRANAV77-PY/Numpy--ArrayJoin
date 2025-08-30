import numpy as np

arr1 = np.array([1,2,3])

arr2 = np.array([4,5,6])

arr = np.stack((arr1,arr2),axis = 1)

print(arr)

# stacking along rows

import numpy as np

arr1 = np.array([1,2,3])

arr2 = np.array([4,5,6])

arr = np.hstack((arr1,arr2))

print(arr)

#stacking along columns

import numpy as np

arr1 = np.array([1,2,3])

arr2 = np.array([4,5,6])

arr = np.vstack((arr1,arr2))

print(arr)

#stacking along height

import numpy as np

arr1 = np.arr([1,2,3])

arr2 = np.arr([4,5,6])

arr = np.dstack((arr1,arr2))

print(arr)