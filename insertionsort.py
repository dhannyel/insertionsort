import time

arreglo = [5, 2, 52, 1, 15, 99, 10, 35, 56, 88]
print "Arreglo inicial: "
print arreglo
def tiempo(func):
def wrapper(*arg):
t1 = time.clock()
res = func(*arg)
t2 = time.clock()
print '%s se tomo %0.3fms' % (func.func_name, (t2-t1)*1000.0)
return res
return wrapper


@tiempo
def insertsort(array):
    for lastsortedelement in range(len(array)-1):
        checked = lastsortedelement
        while array[checked] > array[lastsortedelement + 1] and checked >= 0:
            checked -= 1
        #Insert the number into the correct position
        array[checked+1], array[checked+2 : lastsortedelement+2] = array[lastsortedelement+1], array[checked+1 : lastsortedelement+1]
    return array

insertsort(arreglo)
print "Resultado: "
print arreglo
raw_input()