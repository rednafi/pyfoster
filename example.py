from pyfoster.custom_logger import logfunc
import sys
import pyfoster

@logfunc
def zero_div(a, b=0):
    return a // b


print(zero_div(5))
