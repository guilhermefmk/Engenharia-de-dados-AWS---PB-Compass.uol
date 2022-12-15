'''
Dado o array abaixo, converta-o para um array do tipo int32.
• np.arange(9, dtype=np.float32).reshape(3, 3)

'''

import numpy as np

array = np.arange(9, dtype=np.float32).reshape(3, 3)
print(array.dtype)
array = array.astype('int32')
print(array.dtype)