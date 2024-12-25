import numpy as np

# creating 1D Array
arr1 = np.array([1, 2, 3, 4, 5])
print(arr1)

arr2 = np.array([1, 2, 3, 6, 6])
print(type(arr2))
print(arr2.shape)


print(np.arange(0, 10, 2).reshape(5, 1))

print("addition :", arr1 + arr2)
print("subtraction :", arr1 - arr2)
print("multiplication :", arr1 * arr2)

