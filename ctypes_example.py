##Ctypes: C or C++ WITH PYTHON
import glob
import ctypes
import numpy as np
import platform


path='/home/pa/Desktop/Test/' #Change this line

if platform.system() == 'Windows':
	libr = ctypes.CDLL(path+'sum_example.dll')
elif platform.system() =='Linux':
	libr = ctypes.CDLL(path+'sum_example.so')
elif platform.system()=='Mac':
	libr = ctypes.CDLL(path+'sum_example.dylib')
else:
	print('unrecognized system, .so is used by default')
	libr = ctypes.CDLL(path+'sum_example.dll')


#The documentation about this part is available online. There are some examples of initialisation
 
#Int: 
C_arg1=ctypes.c_int(5)
#Double: 
C_arg2=ctypes.c_double(3.4)
#Int vector: 
PY_arg3=np.array([1,2,3,4])
C_arg3=(ctypes.c_int*len(PY_arg3))(*PY_arg3)
#Double vector:
PY_arg4=np.array([1.1,2.8,3.4])
C_arg4=(ctypes.c_double*len(PY_arg4))(*PY_arg4)
#Matrix: 
PY_arg5=np.array([[0,0,0],[0,0,0]])

PY_arg5=PY_arg5.flatten() 
C_arg5=(ctypes.c_double*len(PY_arg5))(*PY_arg5)


#
#Pointer: 
C_arg1=ctypes.pointer(C_arg1)
C_arg2=ctypes.pointer(C_arg2)
C_arg3=ctypes.pointer(C_arg3)
C_arg4=ctypes.pointer(C_arg4)
C_arg5=ctypes.pointer(C_arg5)

#Matrix dimensions
C_arg6=ctypes.pointer(ctypes.c_int(2))
C_arg7=ctypes.pointer(ctypes.c_int(3))

#Example: a sum function

E_arg1=ctypes.pointer(ctypes.c_int(1))
E_arg2=ctypes.pointer(ctypes.c_int(2))
E_arg3=ctypes.pointer(ctypes.c_int(0))#This is the result variable, witch needs to be initialized with the good type (value by default)

libr.sum(E_arg1,E_arg2,E_arg3)

print(E_arg3[0])#The result variable is a pointer: to find the result, take the first element



    
    
