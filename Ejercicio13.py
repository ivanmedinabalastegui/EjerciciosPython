a = ((1, 2, 3),
    (3, 2, 1))
b = ((1, 2),
    (3, 4),
    (5, 6))
def producto(a, b):
    producto = []
    for i in range(len(a)): # Cambio de "b" a "a"
        fila = []
        for j in range(len(b[0])): # Cambio de "a" a "b"
            suma = 0
            for k in range(len(a[0])): # No es necesario sumar 1
                suma += a[i][k] * b[k][j] # No es necesario sumar 1 a la k
            fila.append(suma) # Con .append añades un objeto a la lista
        producto.append(tuple(fila))
    return tuple(producto)
print(producto(a, b))