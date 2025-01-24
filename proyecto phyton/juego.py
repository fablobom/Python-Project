#crear un juego de ahorcado con lo solicitado

#primer commit

import random

# Lista de palabras para adivinar
palabras = ["python", "ahorcado", "programacion", "desafios", "codigo"]

# Elegir una palabra al azar
palabra_a_adivinar = random.choice(palabras)

# Configurar el estado inicial del juego
letras_adivinadas = []
intentos_restantes = 6
# Función para mostrar el estado actual de la palabra
def mostrar_palabra(palabra, letras_adivinadas):
    estado = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            estado += letra + " "
        else:
            estado += "_ "
    return estado.strip()

# Bucle principal del juego
while intentos_restantes > 0:
    # Mostrar el estado actual de la palabra y los intentos restantes
    print("\nPalabra: ", mostrar_palabra(palabra_a_adivinar, letras_adivinadas))
    print(f"Intentos restantes: {intentos_restantes}")
    
    # Pedir al jugador que adivine una letra
    letra = input("Adivina una letra: ").lower()
    
    # Verificar si ya se ha adivinado esa letra
    if letra in letras_adivinadas:
        print("Ya adivinaste esa letra. Intenta con otra.")
        continue

    # Agregar la letra a la lista de letras adivinadas
    letras_adivinadas.append(letra)
    
    # Comprobar si la letra está en la palabra
    if letra in palabra_a_adivinar:
        print(f"¡Bien hecho! La letra '{letra}' está en la palabra.")
        
        # Verificar si el jugador ha adivinado toda la palabra
        if all(letra in letras_adivinadas for letra in palabra_a_adivinar):
            print("\n¡Felicidades! Adivinaste la palabra:", palabra_a_adivinar)
            break
    else:
        print(f"La letra '{letra}' no está en la palabra.")
        intentos_restantes -= 1

# Verificar si el jugador ha perdido
if intentos_restantes == 0:
    print("\n¡Te has quedado sin intentos! La palabra era:", palabra_a_adivinar)

