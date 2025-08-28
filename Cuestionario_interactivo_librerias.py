
def inicio():
    # --- Inicio ---
    while True:
        print("-----------------------------")
        print("\n=== Bienbenido a mi cuestionario interactivo ===\n")
        print("Las preguntas seran tipo test de -a-, -b-, -c-, y  -d- y estas letras son las que tendras que escribir como respuesta dependiendo cual creas que es la correcta.")
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
    # --- Preguntas ---

    preguntas = [
        {
            "pregunta": "1) ¿Cuál es la capital de España?",
            "opciones": ["a) Barcelona", "b) Valencia", "c) Bilbao", "d) Madrid"],
            "respuesta": "d"
        },
        {
            "pregunta": "2) Selecciona el avión que no opera en el ejército ruso.",
            "opciones": ["a) Su-25", "b) Mig-29", "c) J-17", "d) Tu-160"],
            "respuesta": "c"
        },
        {
            "pregunta": "3) ¿Qué versión del Leopard opera España actualmente?",
            "opciones": ["a) Leopard 2A7HU", "b) Leopard 2E", "c) Leopard 2PL", "d) Leopard 2A7V"],
            "respuesta": "b"
        },
        {
            "pregunta": "4) ¿Cuál de los siguientes misiles es de origen americano?",
            "opciones": ["a) AIM-9L", "b) R60MK", "c) PL-5EII", "d) R-73"],
            "respuesta": "a"
        },
        {
            "pregunta": "5) ¿En cuál de estos aviones Sukhoi los pilotos se sientan lado a lado?",
            "opciones": ["a) Su-25", "b) Su-27", "c) Su-30", "d) Su-34"],
            "respuesta": "d"
        }
    ]
    puntos = 0

    # --- Mostrar preguntas ---

    # Muestra cada pregunta
    for p in preguntas:
        print("-----------------------------")
        print(p["pregunta"])
        for opcion in p["opciones"]:
            print(opcion)
        print("-----------------------------")
        # Ver si la respuesta es valida
        while True:
            respuesta = input("Escribe tu respuesta: ").lower()
            if respuesta in ["a", "b", "c", "d"]:
                break
            else:
                print("Respuesta inválida. Escribe a, b, c o d.")
        #
        if respuesta == p["respuesta"]:
            print("¡Correcto! :) +1 punto")
            puntos += 1
        else:
            print("Incorrecto :(")
    # Guardar resultados
    total = len(preguntas)
    porcentaje = puntos / total * 100

    #-- Puntuacion final --
    print("================================================")
    if puntos == 5:
        print("Enhorabuea has conseguido la puntuacion paxima!!!")
    elif puntos == 4:
        print("Enhorabuea has sacado casi la puntuacion maxima")
    elif puntos == 3:
        print("Enhorabuea has aprobado")
    elif puntos == 2:
        print("Toca estudiar mas para la proxima has suspendido")
    elif puntos == 1:
        print("Almenos una... Estudia para la proxima...")
    else :
        print("Ni la capital de España...")

    print(f"Puntos: {puntos}/{total} ({porcentaje:.2f}%)")
    input("Presiona Enter para volver al inicio...")

inicio()