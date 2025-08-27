
# --- introduccion ---
print("-----------------------------")
print("\n=== Bienbenido a mi cuestionario interactivo ===\n")
print("Las preguntas seran tipo test de -a-, -b-, -c-, y  -d- y estas letras son las que tendras que escribir como respuesta dependiendo cual creas que es la correcta.")
input("Si estas listo presiona Enter para continuar...")

# --- 1ºPregunta ---
print("Cual es la capital de España"
      "a)"
      "b)"
      "C)"
      "D)")
letras = ["a", "b", "c", "d"]
puntos = 0
respuesta = input("Escribe tu respuesta:")
solucion1 = "d"
if respuesta in letras:
    if respuesta == solucion1:
        print("Corecto :) +1punto")
        puntos = puntos + 1
    else:
        print("Error :´(")
else:
    print("Respuesta invalida responde con a, b, c o d")
