
def inicio():
    # --- Inicio ---
    while True:
        print("-----------------------------")
        print("\n=== Bienbenido a mi cuestionario interactivo ===\n")
        print(
            "Las preguntas seran tipo test de -a-, -b-, -c-, y  -d- y estas letras son las que tendras que escribir como respuesta dependiendo cual creas que es la correcta.")
        print("Selecciona una de las siguientes opcione spara continuar escribiendo 1 o 2")
        print("1.-Iniciar cuestionario")
        print("2.-Salir")
        while True:
            respuesta = float(input("Introduce tu respuesta:"))
            if respuesta in [1, 2]:
                break
            else:
                print("Respuesta invalida responde con 1 o 2")
        if respuesta == 1:
            cuestionario()
        else:
            exit()

def cuestionario():
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
    solucion1 = "d"
    while True:
        respuesta = input("Escribe tu respuesta:").lower()
        if respuesta in letras:
            break
        else:
            print("Respuesta invalida responde con a, b, c o d")
    if respuesta == solucion1:
        print("Corecto :) +1punto")
        puntos = puntos + 1
    else:
        print("Error :´(")

    # --- 2ºPregunta ---
    print("-----------------------------")
    print("2) Selecciona el avion que no opera en el ejercito ruso")
    print("a) Su-25")
    print("b) Mig-29")
    print("c) J-17")
    print("d) Tu-160")
    print("-----------------------------")
    solucion2 = "c"
    while True:
        respuesta = input("Escribe tu respuesta:").lower()
        if respuesta in letras:
            break
        else:
            print("Respuesta invalida responde con a, b, c o d")
    if respuesta == solucion2:
        print("Corecto :) +1punto")
        puntos = puntos + 1
    else:
        print("Error :´(")

    # --- 3ºPregunta ---
    print("-----------------------------")
    print("3) Que version del Leopard opera españa actualmente")
    print("a) Leopard 2A7HU")
    print("b) Leopard 2E")
    print("c) Leopard 2PL")
    print("d) Leopard 2A7V")
    print("-----------------------------")
    solucion3 = "b"
    while True:
        respuesta = input("Escribe tu respuesta:").lower()
        if respuesta in letras:
            break
        else:
            print("Respuesta invalida responde con a, b, c o d")
    if respuesta == solucion3:
        print("Corecto :) +1punto")
        puntos = puntos + 1
    else:
        print("Error :´(")
    # --- 4ºPregunta ---
    print("-----------------------------")
    print("4) Cual de los siguientes misiles es de origen Americano")
    print("a) Aim-9L")
    print("b) R60MK")
    print("c) PL-5EII")
    print("d) r-73")
    print("-----------------------------")
    solucion4 = "a"
    while True:
        respuesta = input("Escribe tu respuesta:").lower()
        if respuesta in letras:
            break
        else:
            print("Respuesta invalida responde con a, b, c o d")
    if respuesta == solucion4:
        print("Corecto :) +1punto")
        puntos = puntos + 1
    else:
        print("Error :´(")

    # --- 5ºPregunta ---
    print("-----------------------------")
    print("5) Cual de los siguientes aviones tipo Sukhoi el piloto va uno sentado al lado del otro")
    print("a) Su-25")
    print("b) Su-27")
    print("c) Su-30")
    print("d) Su-34")
    print("-----------------------------")
    solucion5 = "d"
    while True:
        respuesta = input("Escribe tu respuesta:").lower()
        if respuesta in letras:
            break
        else:
            print("Respuesta invalida responde con a, b, c o d")
    if respuesta == solucion5:
        print("Corecto :) +1punto")
        puntos = puntos + 1
    else:
        print("Error :´(")
    #-- Puntuacion final --
    print("================================================")
    if puntos == 5:
        print("Enhorabuea has conseguido la puntuacion paxima!!!")
        print("Puntos: ", puntos)
    elif puntos == 4:
        print("Enhorabuea has sacado casi la puntuacion maxima")
        print("Puntos: ", puntos)
    elif puntos == 3:
        print("Enhorabuea has aprobado")
        print("Puntos: ", puntos)
    elif puntos == 2:
        print("Toca estudiar mas para la proxima has suspendido")
        print("Puntos: ", puntos)
    elif puntos == 1:
        print("Almenos una... Estudia para la proxima...")
        print("Puntos: ", puntos)
    else :
        print("Ni la capital de España...")
        print("Puntos: ", puntos)
    input("Presiona Enter para continuar al inicio...")

inicio()