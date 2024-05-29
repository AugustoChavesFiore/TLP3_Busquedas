
from medir_tiempo import mide_tiempo


@mide_tiempo
def busqueda_binaria(list, target):
    left = 0
    right = len(list) - 1

    while left <= right:
        midpoint = (left + right) // 2

        if list[midpoint] == target:
            return True
        elif list[midpoint] < target:
            left = midpoint + 1
        else:
            right = midpoint - 1
            
    return False

assert busqueda_binaria([1, 2, 3, 4, 5], 1) == True
assert busqueda_binaria([1, 2, 3, 4, 5], 6) == False
assert busqueda_binaria([1, 2, 3, 4, 5], 3) == True
assert busqueda_binaria([1, 2, 3, 4, 5], 5) == True


if __name__ == '__main__':
    print('All test cases pass')

