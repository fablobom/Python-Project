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

