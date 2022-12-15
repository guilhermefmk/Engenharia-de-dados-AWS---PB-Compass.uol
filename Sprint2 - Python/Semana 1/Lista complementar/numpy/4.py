'''
A partir das arrays abaixo, caso seja possível, realize o produto das mesmas:
• np.random.uniform(size=(5, 3))
• np.random.uniform(size=(3, 4))
'''
import numpy as np
array1 = np.random.uniform(size=(5, 3))
array2 = np.random.uniform(size=(3, 4))
result = np.dot(array1,array2)
print(array1)
print(array2)
print(result)