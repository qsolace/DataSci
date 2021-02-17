import numpy as np

test = [3, 4.5, 2.345, -7.233, 1.7]
print (test)
test2 = [21, 3.3, 4.1213]
test2 = np.around(test, 1)
print (test2)
print("----")
print(np.rint(test))
print(np.fix(test))
print(np.floor(test))
print(np.ceil(test))
print(np.trunc(test))
print("------")
test3 = [4, 2.2, 5.98, 1, 4.44]
print(np.add(test, test3))
print(np.multiply(test, [2]))
print(np.power([2], test2))
print(np.reciprocal(.5))
print(np.divide(test, test3))