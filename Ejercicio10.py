base = float(input('Introduce la base imponible de la factura:')) # Hay que poner float ya que sale número decimal

def aplica_iva(base, iva = 21):
    base += base * iva / 100
    return base # Corregimos la operación para qe nos de lo que queremos

print(aplica_iva(base)) # Este print hay que ponerlo al final para que de la solución después de los cambios