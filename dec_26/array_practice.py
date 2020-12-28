import numpy as np

#need to create a random array of 54 elements with 3 different methods
#then reshape

# a = np.random.rand(54)
# print("a: ", a)
# b = np.random.ranf(54)
# print("b: ", b)
# c = np.random.random_sample(54)
# print("c: ", c)
#
# a = np.reshape(a, (6, 9))
# print(a)
b = np.arange(54)
print(b)
a = np.random.rand(5, 5)
print(a.sum(0))
print(a.sum(1))