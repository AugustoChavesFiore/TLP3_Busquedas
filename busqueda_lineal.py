from medir_tiempo import mide_tiempo


@mide_tiempo
def busqueda_lineal(list, target):
    match = False
    for i in range(len(list)):
        if list[i] == target:
            match = True
            break

    return match

assert busqueda_lineal([1, 2, 3, 4, 5], 1) == True
assert busqueda_lineal([1, 2, 3, 4, 5], 6) == False
assert busqueda_lineal([1, 2, 3, 4, 5], 3) == True
assert busqueda_lineal([1, 2, 3, 4, 5], 5) == True
assert busqueda_lineal([1, 2, 3, 4, 5], 2) == True


if __name__ == '__main__':
    print('All test cases pass')
   