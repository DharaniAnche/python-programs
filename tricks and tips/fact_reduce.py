#!/bin/bash
#----printing factorial of a number----
#reduce is in functools module
#using reduce(fun, seq)
import functools  
n=5
print(functools.reduce(lambda x, y: x * y, range(1, n+1)))
