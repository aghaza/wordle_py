''' Este es el archivo principal del juego WORDLE implementado en python.
    Depende del archivo fuente "bolsa.pkl" que debió ser generado previamente por el código en
    generador.py, que a su vez genera las palabras a partir de un archivo dado a elección.
    De no hallarse el archivo "bolsa.pkl" se intentará generar llamando al generador antedicho.
    Si el jugador ya existe, tiene su propia bolsa de palabras en el archivo {player}.pkl
    En ese archivo, nombrado {nombre_del_jugador}.pkl se almacena su progreso (palabras acertadas,
    palabras erradas, su nombre, su clave, la bolsa de palabras restantes por jugar y su nivel).
    A mayor nivel que alcance un jugador se le irán recortando los intentos posibles para
    acertar la palabra.

    Creado por George Aghazarian - aghazarian@pm.me
    Última versión: 21 de noviembre de 2025 - 18:30

    Archivos imprescindibles con al menos un jugador registrado (no se permitirán nuevos registros):
        main.py
        {player}.pkl

    Archivos imprescindibles en la carpeta si no hay jugadores registrados:
        main.py
        bolsa.pkl
      
    Archivos totales:
        main.py         		- programa principal
        generador.py    		- genera la base de palabras bolsa.pkl a partir de un archivo a elegir que contenga las palabras
        agregador.py    		- gestor del archivo bolsa.pkl que permite agregar, eliminar, contabilizar y listar las palabras
        sugerencias.py			- receptor de sugerencias de palabras
        conversor.py    		- convierte bolsa.pkl a bolsa_set.py cuyo contenido es bolsa = {aquí dentro un set con las palabras}
        list2bin.py				- proceso iverso a conversor.py
        wordsJS_to_pyPKL.py		- igual a list2bin.py pero a partir de words.js
        bolsaPKL_to_wordsJS.py	- proceso inverso a wordsJS_to_pyPKL.py
        bolsa.pkl       		- archivo que contiene la fuente de palabras original para crear un jugador
        frecuentes.txt  		- base de las palabras más frecuentes del castellano
        es.dic          		- corrector ortográfico de LibreOfiice para usar de base de miles de plabras
        icono.png       		- icono de WORDLE

    Requiere python3
'''

from os import system, path
if system("clear") != 0: system("cls")  # Limpiar pantalla
import sys
import subprocess
import pickle
import random
import getpass

# Definiendo estilo de texto:
# Estilos de texto
bold  = "\033[1m"
reset = "\033[0m"
subr  = "\033[4m"
cursiva = "\033[3m"

# Colores de texto
verde = "\033[32m"
azul  = "\033[34m"
rojo  = "\033[31m"
amarillo = "\033[33m"
naranja = "\033[38;5;214m"

# Colores adicionales
cyan = "\033[1;36m"          # Cyan
magenta = "\033[35m"       # Magenta
gris = "\033[37m"          # Gris
blanco = "\033[97m"        # Blanco brillante
negro = "\033[90m"         # Negro brillante

# Colores de fondo
fondo_verde = "\033[42m"   # Fondo verde
fondo_azul = "\033[44m"    # Fondo azul
fondo_rojo = "\033[41m"    # Fondo rojo
fondo_amarillo = "\033[43m" # Fondo amarillo
fondo_naranja = "\033[48;5;214m" # Fondo naranja
fondo_cyan = "\033[46m"    # Fondo cyan
fondo_magenta = "\033[45m" # Fondo magenta
fondo_gris = "\033[47m"    # Fondo gris
fondo_blanco = "\033[107m" # Fondo blanco brillante
fondo_negro = "\033[40m"   # Fondo negro




acertadas = []
erradas = []
bolsa = set()


def salir():
    sys.exit()




def intento(intentada, palabra_secreta):
    resultado = []
    correctas = []
    for i, letra in enumerate(intentada):
        if letra == palabra_secreta[i]:
            resultado.append('🟢')
            correctas.append(letra)
        elif letra in palabra_secreta and letra not in correctas:
            resultado.append('?')
        else:
            resultado.append('🔴')
    for i, letra in enumerate(intentada):
    	if resultado [i] == '?' and letra in correctas:
    		resultado [i] = '🔴'
    	elif resultado [i] == '🟢':
    		None
    	elif resultado [i] == '🔴':
    			None    			
    	else:
    		resultado [i] = '🟡'
    print (resultado)
    print (correctas)
    return resultado

resultado = False

# Límite de intentos
limite_intentos = 1000

# Ciclo del juego
while True:


    palabra_secreta = 'errro'
    print(f'Palabra secreta: {palabra_secreta}')  # Para depuración


    print(f'{bold}\nWORDLE{reset} de 5 letras.\nTenés {limite_intentos} intentos.\n\n{naranja}Ingresá una {bold} X {reset}{naranja} en cualquier momento para salir.{reset} \n{blanco}¡¡La {reset}{bold}Ñ{reset}{blanco} también existe!!{reset}\n\n🟢 {verde}letra correcta en la posición correcta\n🟡 {amarillo}letra correcta en la posición equivocada\n🔴 {rojo}la letra no está en la palabra.{reset}\n')
    print(len(bolsa) + 1, f'palabras posibles.\n{bold}¡¡MUCHA SUERTE!!{reset}')

    intentos = 0
    while intentos < limite_intentos:
        palabra_adivinada = input('\n\npalabra: ')
        intentos += 1
        print(limite_intentos - intentos, 'intentos restantes...\n')
        resultado = intento(palabra_adivinada, palabra_secreta)
        print(f"Resultado: {''.join(resultado)}")

        if resultado == True:
            
            print(f'\n 🎊 {bold}{verde}¡¡¡FELICITACIONES!!!{reset} 🎊')
            break
    else:
        

        print(f'\n🔥 {bold}{cyan}{fondo_naranja}CAGASTE FUEGO{reset} 🔥\nLa palabra era: {bold}{azul}{palabra_secreta.upper()}{reset}')

    # Preguntar siempre si quiere volver a jugar
    while True:
        volver = input(f'\n{bold}¿Querés jugar de nuevo? (s/n): {reset}').strip().lower()
        if volver == 's':
            break
        elif volver == 'n' or volver == 'x':
            print('\n¡Hasta luego! 👋 \n')
            salir()
        else:
            print(f'{rojo}Opción no válida. Ingresá "s" o "n".{reset}')
