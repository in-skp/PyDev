import numpy as np
print(np.array([1.0, "is", True]))
py_list = [1, 2, 3]
print(py_list + py_list)
np_array = np.array([1, 2, 3])
print(np_array + np_array)
height = [1.73, 1.68, 1.71, 1.89, 1.79]
np_height = np.array(height)
weight = [65.4, 59.2, 63.6, 88.4, 68.7]
np_weight = np.array(weight)
bmi = np_weight / np_height ** 2
print(bmi)
print(bmi > 23)
print(bmi[bmi > 21])
print(type(bmi))
np_2d = np.array([[1.73, 1.68, 1.71, 1.89, 1.79],
                  [65.4, 59.2, 63.6, 88.4, 68.7]])
print(np_2d)
print(np_2d.shape)
print(np_2d[0])
print(np_2d[0][2])
print(np_2d[0, 2])
print(np_2d[:, 1:3])
print(np_2d[1, :])

height = np.round(np.random.normal(1.75, 0.20, 5000), 2)
print(height)
print(np.mean(height))
print(np.array([True, 1, 2]) + np.array([3, 4, False]))
