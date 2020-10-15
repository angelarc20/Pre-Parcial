from clave_X.clave_x import suma, multiplicacion, sumarLista, getGithubUrl

result = suma(2, 4)
if result == 6:
    print("ejercicio01: pass")
else:
    print("ejercicio01: fail")

result = multiplicacion(2, 4, 5)
if result == 40:
    print("ejercicio02: pass")
else:
    print("ejercicio02: fail")

numerosLista = [2, 5, 4, 6, 9, 12]
result = sumarLista(2, 5, 4, 6, 9, 12)
if result == 38:
    print("ejercicio03: pass")
else:
    print("ejercicio03: fail")

result = getGithubUrl("https://github.com/angelarc20/Pre-Parcial.git")
if not result == "":
    print("ejercicio04: pass")
else:
    print("ejercicio04: fail")
