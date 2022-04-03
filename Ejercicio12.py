listin = {'Juan':123456789, 'Pedro':987654321}
def elimina(listin, usuario):
    return listin.pop(usuario, '') # No es necesario poner la línea eliminada ya que con .pop se elimina lo que indiques de la lista

print(elimina(listin, 'Pablo'))