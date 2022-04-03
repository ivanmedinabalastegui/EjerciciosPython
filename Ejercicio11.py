u = [1, 2, 3]
v = [4, 5, 6] # Las listas se hacen con corchetes
def producto_escalar(u, v):
    for i in range(len(u)): # Lo ponemos de esta forma para que se ejecute tantas veces como larga sea la lista
        u[i] *= v[i] # No hace falta poner el +1
    return sum(u)
print(producto_escalar(u, v))