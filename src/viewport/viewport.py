#!/usr/bin/env python3
from ctypes import byref, c_double, c_int, CDLL
import sys
import os.path

lib_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'viewport.so')
#lib_path = 'viewport.so'
basic_function_lib = CDLL(lib_path)

python_c_square = basic_function_lib.c_square
python_c_square.restype = None

class ViewportApp:
    def __init__(self, window_size):
        error_code = c_int(0)
        self.window_size = window_size
        self._as_parameter_ = basic_function_lib.initSDL(
                byref(error_code),
                c_int(window_size[0]),
                c_int(window_size[1]))

        if not self._as_parameter_:
            raise Exception(error_code.value)

    def __repr__(self):
        return '<ViewportApp[{}, {}]>'.format(self.window_size[0], self.window_size[1])

class Viewport:
    def __init__(self):
        #self.viewportapp = ViewportApp()
        self.viewportapp = ViewportApp( (400, 300) )
        print(self.viewportapp)

def do_square_using_c(list_in):
    n = len(list_in)
    c_arr_in = (c_double * n)(*list_in)
    c_arr_out = (c_double * n)()
    python_c_square(c_int(n), c_arr_in, c_arr_out)
    return c_arr_out[:]

if __name__ == '__main__':
    print(do_square_using_c([2.0, 2.2, 3.0, 4.0]))
    Viewport()
    input()
