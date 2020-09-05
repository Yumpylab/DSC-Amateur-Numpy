Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as np
>>> my_list= [1,2,3,4,5]
>>> my_numpy_list= np.array(my_list)
>>> my_numpy_list
array([1, 2, 3, 4, 5])
>>> 
>>> second_list= [[1,2,3],[5,4,1], [3,6,7]]
>>> new_2d_arr= np.array(second_list)
>>> new_2d_arr
array([[1, 2, 3],
       [5, 4, 1],
       [3, 6, 7]])
>>> 
>>> my_list= np.arange(10)
>>> my_list
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> my_list= np.arange(0,10)
>>> my_list
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> my_list= np.arange(0,11,2)
>>> my_list
array([ 0,  2,  4,  6,  8, 10])
>>> 
>>> my_zeros= np.zeros(7)
>>> my_zeros
array([0., 0., 0., 0., 0., 0., 0.])
>>> 
>>> my_ones= np.ones(5)
>>> my_ones
array([1., 1., 1., 1., 1.])
>>> two_d= np.zeros((3,5))
>>> two_d
array([[0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0.]])
>>> 
>>> lin_arr= np.linspace(1,3,15)
>>> lin_arr
array([1.        , 1.14285714, 1.28571429, 1.42857143, 1.57142857,
       1.71428571, 1.85714286, 2.        , 2.14285714, 2.28571429,
       2.42857143, 2.57142857, 2.71428571, 2.85714286, 3.        ])
>>> linspace(1,15,3)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    linspace(1,15,3)
NameError: name 'linspace' is not defined
>>> np.linspace91,15,3)
SyntaxError: unmatched ')'
>>> np.linspace(1,15,3)
array([ 1.,  8., 15.])
>>> np.linspace(0,15,4)
array([ 0.,  5., 10., 15.])
>>> 
>>> 
>>> my_matrix= np.eye(6)
>>> my_matrix
array([[1., 0., 0., 0., 0., 0.],
       [0., 1., 0., 0., 0., 0.],
       [0., 0., 1., 0., 0., 0.],
       [0., 0., 0., 1., 0., 0.],
       [0., 0., 0., 0., 1., 0.],
       [0., 0., 0., 0., 0., 1.]])
>>> np.eye(3)
array([[1., 0., 0.],
       [0., 1., 0.],
       [0., 0., 1.]])
>>> 
>>> 
>>> np.random.rand(5)
array([0.50818827, 0.2415204 , 0.93523924, 0.67906591, 0.97125708])
>>> np.random.rand(5,4)
array([[0.42579819, 0.86114987, 0.36827421, 0.93852711],
       [0.11585508, 0.10384592, 0.40184448, 0.66813852],
       [0.36538524, 0.8181313 , 0.17236839, 0.84898307],
       [0.10606948, 0.98594292, 0.56941174, 0.71928818],
       [0.02556575, 0.24986632, 0.26261435, 0.50753816]])
>>> 
>>> np.random.randn(7)
array([-1.738022  ,  1.55834641, -0.12270971, -0.19595442,  0.44278097,
        0.14598537, -0.34329721])
>>> np.random.randn(3,5)
array([[-0.03534763, -0.2041252 , -0.67791077,  0.8774147 , -0.34724434],
       [-1.31221938, -0.37533647,  0.41725754, -1.19162094, -0.55954675],
       [-0.77369952, -0.1380581 , -0.22852858,  0.24862905, -0.1642307 ]])
>>> 
>>> 
>>> np.random.randint(20)
16
>>> np.random.randint(2,20)
19
>>> np.random.randint(2,20,7)
array([ 8,  2, 16, 18,  5,  5,  8])
>>> 
>>> 
>>> arr= np.random.rand(25)
>>> arr.reshape
<built-in method reshape of numpy.ndarray object at 0x0737CCA0>
>>> arr.reshape(5,5)
array([[0.27938117, 0.24588169, 0.64433756, 0.60974732, 0.21557214],
       [0.39367068, 0.47802692, 0.029343  , 0.00269951, 0.49689502],
       [0.31431932, 0.56105111, 0.47877146, 0.56544831, 0.426341  ],
       [0.81156625, 0.39303406, 0.47064059, 0.94257178, 0.80663123],
       [0.03901304, 0.47142382, 0.34901945, 0.45636334, 0.31361471]])
>>> arr
array([0.27938117, 0.24588169, 0.64433756, 0.60974732, 0.21557214,
       0.39367068, 0.47802692, 0.029343  , 0.00269951, 0.49689502,
       0.31431932, 0.56105111, 0.47877146, 0.56544831, 0.426341  ,
       0.81156625, 0.39303406, 0.47064059, 0.94257178, 0.80663123,
       0.03901304, 0.47142382, 0.34901945, 0.45636334, 0.31361471])
>>> arr.reshape(5,5)
array([[0.27938117, 0.24588169, 0.64433756, 0.60974732, 0.21557214],
       [0.39367068, 0.47802692, 0.029343  , 0.00269951, 0.49689502],
       [0.31431932, 0.56105111, 0.47877146, 0.56544831, 0.426341  ],
       [0.81156625, 0.39303406, 0.47064059, 0.94257178, 0.80663123],
       [0.03901304, 0.47142382, 0.34901945, 0.45636334, 0.31361471]])
>>> arr_2 = np.random.randint(0,20,10)
>>> arr_2
array([19, 18, 11, 15,  2,  2,  9,  2,  4,  3])
>>> arr_2.max()
19
>>> arr_2.min()
2
>>> arr_2.argmax()
0
>>> arr_2.argmin()
4
>>> arr.shape
(25,)
>>> 
>>> 
>>> my_array = np.arange(0,11)
>>> my_array
array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10])
>>> my_array[8]
8
>>> my_array[2:6]
array([2, 3, 4, 5])
>>> my-array[:6]
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    my-array[:6]
NameError: name 'my' is not defined
>>> my_array[:6]
array([0, 1, 2, 3, 4, 5])
>>> my_array[5:]
array([ 5,  6,  7,  8,  9, 10])
>>> 
>>> two_d_arr = np.array([[10,20,30],[40,50,60], [70,80,90]])
>>> two_d_arr
array([[10, 20, 30],
       [40, 50, 60],
       [70, 80, 90]])
>>> two_d_arr
array([[10, 20, 30],
       [40, 50, 60],
       [70, 80, 90]])
>>> two_d_arr(0,1)
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    two_d_arr(0,1)
TypeError: 'numpy.ndarray' object is not callable
>>> two_d_arr[0,1]
20
>>> two_d_[:1, :2]
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    two_d_[:1, :2]
NameError: name 'two_d_' is not defined
>>> two_d_arr[:1, :2]
array([[10, 20]])
>>> two_d_arr[:2, :3]
array([[10, 20, 30],
       [40, 50, 60]])
>>> two_d_arr[:2, 1:]
array([[20, 30],
       [50, 60]])
>>> two_d_arr[0]
array([10, 20, 30])
>>> two_d_arr[:2]
array([[10, 20, 30],
       [40, 50, 60]])
>>> 
>>> 
>>> new_arr= np.arange(5,15)
>>> new_arr
array([ 5,  6,  7,  8,  9, 10, 11, 12, 13, 14])
>>> new_arr > 10
array([False, False, False, False, False, False,  True,  True,  True,
        True])
>>> bool_arr= new_arr > 10
>>> bool_arr
array([False, False, False, False, False, False,  True,  True,  True,
        True])
>>> new_arr[bool_arr]
array([11, 12, 13, 14])
>>> new_arr[new-arr > 10]
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    new_arr[new-arr > 10]
NameError: name 'new' is not defined
>>> new_arr[new_arr > 10]
array([11, 12, 13, 14])
>>> new_arr[(new_arr >6) & (new_arr<10)]
array([7, 8, 9])
>>> 
>>> 
>>> my_array[0:3] = 50
>>> my_array
array([50, 50, 50,  3,  4,  5,  6,  7,  8,  9, 10])
>>> 
>>> 
>>> arr= np.arange(1,11)
>>> arr * arr
array([  1,   4,   9,  16,  25,  36,  49,  64,  81, 100])
>>> arr-arr
array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
>>> arr + arr
array([ 2,  4,  6,  8, 10, 12, 14, 16, 18, 20])
>>> arr/arr
array([1., 1., 1., 1., 1., 1., 1., 1., 1., 1.])
>>> 
>>> 
>>> arr + 50
array([51, 52, 53, 54, 55, 56, 57, 58, 59, 60])
>>> np.sqrt(arr)
array([1.        , 1.41421356, 1.73205081, 2.        , 2.23606798,
       2.44948974, 2.64575131, 2.82842712, 3.        , 3.16227766])
>>> np.exp(arr)
array([2.71828183e+00, 7.38905610e+00, 2.00855369e+01, 5.45981500e+01,
       1.48413159e+02, 4.03428793e+02, 1.09663316e+03, 2.98095799e+03,
       8.10308393e+03, 2.20264658e+04])
>>> np.sin(arr)
array([ 0.84147098,  0.90929743,  0.14112001, -0.7568025 , -0.95892427,
       -0.2794155 ,  0.6569866 ,  0.98935825,  0.41211849, -0.54402111])
>>> np.sin(30)
-0.9880316240928618
>>> np.sin(60)
-0.3048106211022167
>>> np.sin(90)
0.8939966636005579
>>> sin(30)
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    sin(30)
NameError: name 'sin' is not defined
>>> np.cos(arr)
array([ 0.54030231, -0.41614684, -0.9899925 , -0.65364362,  0.28366219,
        0.96017029,  0.75390225, -0.14550003, -0.91113026, -0.83907153])
>>> np.sum(arr)
55
>>> np.std(arr)
2.8722813232690143
>>> mat= np.arange(1,26).reshape(5,5)
>>> mat.sum()
325
>>> mat.sum(axis=0)
array([55, 60, 65, 70, 75])
>>> mat.sum(axis=1)
array([ 15,  40,  65,  90, 115])
>>> 