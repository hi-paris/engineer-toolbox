##Ctypes Readme

How to use Ctypes:

Your code can be write in C or C++.


Ctypes works only with C, but, by writing extern "C" { [CODE]}, C++ can be interpreted in C++.


Compilation:
First, you must compile your code.

After, you must create a shared library. The extension of a shared library depends of your exploration system:

.so in Linux
.dll in Windows
.dylib in MacOs

In Linux, the following commands works:

g++ -c -fpic sum_example.cpp
g++ -shared sum_example.o -o sum_example.so
After having your shared library, you have to call it by using ctypes.
The ctypes function called CDLL can call your library (you have to put your path in argument.) :
libr = ctypes.CDLL(path+'sum_example.so')

To call a C++ function in Python, you must transform your argument from python's types to Ctypes object.

To do it, you must use this function: ctypes.c_int(5)

The list of all types is available here: https://docs.python.org/3/library/ctypes.html#fundamental-data-types


For the array, you have to initialize the length and after initialize the value:

Vect=np.array([1.1,2.8,3.4])
Vect_ctypes=(ctypes.c_double*len(Vect))(*Vect)

Your function is an object of your class "libr": libr.function(ctypes_arg1,ctypes_arg2,ctypes_arg3)

You have to initialize your result: the return of the C++ function has to include in your argument.
