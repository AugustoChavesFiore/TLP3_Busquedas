# Busquedas Binarias y Lineales

1. Clonar Repositorio 
2. Probar los archivos con py ej:
``` 
py busqueda_binaria.py
```


## Busqueda Binaria
En este caso, este tipo de búsqueda es usado en listas que estén previamente ordenadas, ya que su método de búsqueda es la de dividir los datos en dos grupos, eligiendo el grupo en el cual debería estar el dato buscado (supone que está ordenado alfabéticamente o numericamente), volviendo a aplicar la división, y así sucesivamente hasta verificar si existe o no existe el dato buscado.

## Busqueda Lineal 
Este tipo de algoritmo, como su nombre indica, busca desde el primer dato hasta el último, uno a uno comparando sucesivamente todos los datos en memoria hasta localizar el dato que queramos localizar. Este algoritmo puede usarse en cualquier situación, pero se recomienda usarlo solo en listas que no estén ordenadas, ya que para las que lo estén podremos usar el siguiente algoritmo, que es mucho más eficiente


# Decorador de medir tiempo
Esta funcion nos permite medir el tiempo de ejecucion de otras funciones a traves de un decorador, arrojando el tiempo de ejecucion cada ves que se usa un funcion x.
