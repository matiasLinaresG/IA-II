# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 22:43:10 2023

@author: Usuario
"""

import time
import multiprocessing as mt


def calculate(func, args):
    result = func(*args)
    return '%s says that %s%s = %s' % (
        mt.current_process().name,
        func.__name__, args, result
        )

def calculatestar(args):
    return calculate(*args)

def f(x,y):
    return x+y

if __name__ == '__main__':
    
    lista = [(f, (i, 7)) for i in range(10)]
    with mt.Pool(processes=2) as pool:
        
        test1 = pool.apply_async(calculate, lista[0])
        print(test1.get(timeout=1))
        
        print(pool.map(calculatestar, lista))
        
test1 = pool.apply_async(
    calculate, tareas[0])
try:
    print(test1.get(timeout=40))
except multiprocessing.TimeoutError:
    print("Se acabo el tiempo")