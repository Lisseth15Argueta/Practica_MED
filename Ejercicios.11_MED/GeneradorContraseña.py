import random
import string

def generar_contrasena(longitud):
    caracteres = string.ascii_letters + string.digits
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

longitud_contrasena = 20
contrasena_generada = generar_contrasena(longitud_contrasena)
print("Contraseña generada:", contrasena_generada)