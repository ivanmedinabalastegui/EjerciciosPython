a = (1, 2, 3)
b = (-1, 0, 2)
product = 0
product2 = 0
for i in range(len(a)):
    product = a[i-1]*b[i-1]
    product2 = product + product2

print("El producto de los vectores " + str(a) + " y " + str(b) + " es " + str(product2))