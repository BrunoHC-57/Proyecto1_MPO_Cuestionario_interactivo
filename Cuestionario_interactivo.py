
# --- introduccion ---
print("-----------------------------")
print("\n=== Bienbenido a mi cuestionario interactivo ===\n")
print("Las preguntas seran tipo test de -a-, -b-, -c-, y  -d- y estas letras son las que tendras que escribir como respuesta dependiendo cual creas que es la correcta.")
input("Si estas listo presiona Enter para continuar...")

# --- 1ºPregunta ---
print("-----------------------------")
print("1) Cual es la capital de España")
print("a)Barcelona")
print("b)Valencia")
print("c)Bilbao")
print("d)Madrid")
print("-----------------------------")
letras = ["a", "b", "c", "d"]
puntos = 0
respuesta = input("Escribe tu respuesta:").lower()
solucion1 = "d"
if respuesta in letras:
    if respuesta == solucion1:
        print("Corecto :) +1punto")
        puntos = puntos + 1
    else:
        print("Error :´(")
else:
    print("Respuesta invalida responde con a, b, c o d")

# --- 2ºPregunta ---
print("-----------------------------")
print("2) Selecciona el avion que no opera en el ejercito ruso")
print("a) Su-25")
print("b) Mig-29")
print("c) J-17")
print("d) Tu-160")
print("-----------------------------")
respuesta = input("Escribe tu respuesta:").lower()
solucion2 = "c"
if respuesta in letras:
    if respuesta == solucion2:
        print("Corecto :) +1punto")
        puntos = puntos + 1
    else:
        print("Error :´(")
else:
    print("Respuesta invalida responde con a, b, c o d")

# --- 3ºPregunta ---
print("-----------------------------")
print("3) Que version del Leopard opera españa actualmente")
print("a) Leopard 2A7HU")
print("b) Leopard 2E")
print("c) Leopard 2PL")
print("d) Leopard 2A7V")
print("-----------------------------")
respuesta = input("Escribe tu respuesta:").lower()
solucion3 = "b"
if respuesta in letras:
    if respuesta == solucion3:
        print("Corecto :) +1punto")
        puntos = puntos + 1
    else:
        print("Error :´(")
else:
    print("Respuesta invalida responde con a, b, c o d")
# --- 4ºPregunta ---
print("-----------------------------")
print("4) Cual de los siguientes misiles es de origen Americano")
print("a) Aim-9L")
print("b) R60MK")
print("c) PL-5EII")
print("d) r-73")
print("-----------------------------")
respuesta = input("Escribe tu respuesta:").lower()
solucion4 = "a"
if respuesta in letras:
    if respuesta == solucion4:
        print("Corecto :) +1punto")
        puntos = puntos + 1
    else:
        print("Error :´(")
else:
    print("Respuesta invalida responde con a, b, c o d")

# --- 5ºPregunta ---
print("-----------------------------")
print("5) Cual de los siguientes aviones tipo Sukhoi el piloto va uno sentado al lado del otro")
print("a) Su-25")
print("b) Su-27")
print("c) Su-30")
print("d) Su-34")
print("-----------------------------")
respuesta = input("Escribe tu respuesta:").lower()
solucion5 = "d"
if respuesta in letras:
    if respuesta == solucion5:
        print("Corecto :) +1punto")
        puntos = puntos + 1
    else:
        print("Error :´(")
else:
    print("Respuesta invalida responde con a, b, c o d")
