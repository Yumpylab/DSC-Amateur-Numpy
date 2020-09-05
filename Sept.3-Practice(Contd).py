Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as np
>>> a=np.array([1,2,3,4])
>>> b= np.array([3,3,3])
>>> np.concatenate((a,b))
array([1, 2, 3, 4, 3, 3, 3])
>>> a= np.array([1,2,3,4])
>>> b= np.array([3,3,3,3])
>>> np.concatenate((a.reshape(-1,1), b.reshape(-1,1)), axis=1)
array([[1, 3],
       [2, 3],
       [3, 3],
       [4, 3]])
>>> np.concatenate((a.reshape(-1,1), b.reshape(-1,1)), axis=0)
array([[1],
       [2],
       [3],
       [4],
       [3],
       [3],
       [3],
       [3]])
>>> 
>>> 
>>> a= np.array([1,2,3,4])
>>> b= np.array([3,3,3,3])
>>> c= np.array([0,1,5,6])
>>> np.vstack((a,b,c))
array([[1, 2, 3, 4],
       [3, 3, 3, 3],
       [0, 1, 5, 6]])
>>> A=np.random.randint(5, size(2,2,2))
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    A=np.random.randint(5, size(2,2,2))
NameError: name 'size' is not defined
>>> A= np.random.randint(5, size=(2,2,2))
>>> A
array([[[4, 0],
        [0, 3]],

       [[2, 4],
        [3, 2]]])
>>> B= np.random.randint(5, size=(2,2,2))
>>> B
array([[[4, 1],
        [2, 3]],

       [[4, 3],
        [4, 3]]])
>>> C= np.random.randint(5, size=(2,2,2))
>>> C
array([[[0, 2],
        [4, 4]],

       [[3, 4],
        [4, 0]]])
>>> np.vstack((A,B,C))
array([[[4, 0],
        [0, 3]],

       [[2, 4],
        [3, 2]],

       [[4, 1],
        [2, 3]],

       [[4, 3],
        [4, 3]],

       [[0, 2],
        [4, 4]],

       [[3, 4],
        [4, 0]]])
>>> D= np.random.randint(5, size=(2,2,3))
>>> D
array([[[0, 1, 3],
        [4, 3, 3]],

       [[4, 0, 4],
        [3, 2, 4]]])
>>> E= np.random.randint(5, size=(3,2,2))
>>> E
array([[[4, 3],
        [4, 0]],

       [[4, 3],
        [0, 2]],

       [[2, 3],
        [0, 4]]])
>>> 
>>> 
>>> a= np.array([1,2,3,4]).reshape(-1,1)
>>> b= np.array([3,3,3,3]).reshape(-1,1)
>>> c= np.array([0,1,5,6]).rehsape(-1,1)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    c= np.array([0,1,5,6]).rehsape(-1,1)
AttributeError: 'numpy.ndarray' object has no attribute 'rehsape'
>>> a= np.array([1,2,3,4]).reshapw(-1,1)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    a= np.array([1,2,3,4]).reshapw(-1,1)
AttributeError: 'numpy.ndarray' object has no attribute 'reshapw'
>>> a=np.array([1,2,3,4]).reshape(-1,1)
>>> a
array([[1],
       [2],
       [3],
       [4]])
>>> a=np.array([1,2,3,4]).reshape(-1,1)
>>> b=np.array([3,3,3,3]).reshape(-1,1)
>>> c=np.array([0,1,5,6]).reshape(-1,1)
>>> np.hstack((a,b,c))
array([[1, 3, 0],
       [2, 3, 1],
       [3, 3, 5],
       [4, 3, 6]])
>>> 
>>> #Linear algebra with NumPy Arrays (numpy.linalg)
>>> A= np.random.randint(5, size=(3,3))
>>> A
array([[3, 0, 3],
       [4, 0, 4],
       [1, 3, 0]])
>>> np.linalg.det(A)
0.0
>>> np.linalg.inv(A)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    np.linalg.inv(A)
  File "<__array_function__ internals>", line 5, in inv
  File "C:\Users\KALESANWO YOMI\AppData\Local\Programs\Python\Python38-32\lib\site-packages\numpy\linalg\linalg.py", line 546, in inv
    ainv = _umath_linalg.inv(a, signature=signature, extobj=extobj)
  File "C:\Users\KALESANWO YOMI\AppData\Local\Programs\Python\Python38-32\lib\site-packages\numpy\linalg\linalg.py", line 88, in _raise_linalgerror_singular
    raise LinAlgError("Singular matrix")
numpy.linalg.LinAlgError: Singular matrix
>>> A
array([[3, 0, 3],
       [4, 0, 4],
       [1, 3, 0]])
>>> np.linalg.inv(A)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    np.linalg.inv(A)
  File "<__array_function__ internals>", line 5, in inv
  File "C:\Users\KALESANWO YOMI\AppData\Local\Programs\Python\Python38-32\lib\site-packages\numpy\linalg\linalg.py", line 546, in inv
    ainv = _umath_linalg.inv(a, signature=signature, extobj=extobj)
  File "C:\Users\KALESANWO YOMI\AppData\Local\Programs\Python\Python38-32\lib\site-packages\numpy\linalg\linalg.py", line 88, in _raise_linalgerror_singular
    raise LinAlgError("Singular matrix")
numpy.linalg.LinAlgError: Singular matrix
>>> A=np.random.randint(5, size=(3,3))
>>> A
array([[4, 0, 2],
       [3, 3, 4],
       [3, 4, 0]])
>>> np.linalg.det(A)
-57.999999999999986
>>> np.linalg.inv(A)
array([[ 0.27586207, -0.13793103,  0.10344828],
       [-0.20689655,  0.10344828,  0.17241379],
       [-0.05172414,  0.27586207, -0.20689655]])
>>> 
>>> 
>>> np.linalg.eig(A)
(array([ 7.27915959,  2.68662531, -2.9657849 ]), array([[ 0.33946912,  0.59236117, -0.24627145],
       [ 0.75826904, -0.70554255, -0.45126226],
       [ 0.55658672, -0.38899608,  0.85773699]]))
>>> [ 0.55658672, -0.38899608,  0.85773699]]))
SyntaxError: unmatched ']'
>>> np.linalg.eig(A)
(array([ 7.27915959,  2.68662531, -2.9657849 ]), array([[ 0.33946912,  0.59236117, -0.24627145],
       [ 0.75826904, -0.70554255, -0.45126226],
       [ 0.55658672, -0.38899608,  0.85773699]]))
>>> 
>>> 
>>> a=np.array([1,2,3,4])
>>> b=np.array([2,2,2,2])
>>> np.dot(a,b)
20
>>> 
>>> 
>>> A= ([[1,2],[3,4]])
>>> B= ([[3,4],[3,1]])
>>> np.matmul(A,B)
array([[ 9,  6],
       [21, 16]])
>>> 