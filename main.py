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



# Comprobación de la existencia del archivo de bolsa de palabras
if path.exists('bolsa.pkl'):
    # Recuperación del archivo bolsa de palabras
    with open('bolsa.pkl', 'rb') as archivo:
        bolsa = pickle.load(archivo)
else:
    print(f'No se ha encontrado la base de datos {verde}"bolsa.pkl"{reset}.\nSe intentará regenerar base de palabras...\n')
    try:
        # Redirigir la salida y el error a DEVNULL
        subprocess.run(['python3', 'generador.py'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        with open('bolsa.pkl', 'rb') as archivo:
            bolsa = pickle.load(archivo)
    except subprocess.CalledProcessError:  # Solo captura la excepción sin imprimirla
        print(f'{bold}{rojo}No se ha encontrado el generador de palabras\nERROR CRÍTICO\n{reset}\nSaliendo.\n')
        sys.exit()

def cargar_bolsa():
    # Carga la bolsa desde el archivo
    with open('bolsa.pkl', 'rb') as archivo:
        return pickle.load(archivo)

if len(bolsa) == 0:
    bolsa = cargar_bolsa()

class Jugador:
    def __init__(self, n, c, b = bolsa, a = None, e = None, lv = 0):
        self.nombre = n
        self.clave = c
        self.bolsa = b
        self.acertadas = a if a is not None else []
        self.erradas = e if e is not None else []
        self.nivel = 0
        self.calcular_nivel()
    
    def __str__(self):
        txt = (
            f'\n{bold}Jugador:{reset} {self.nombre}' +
            f'\n{bold}Nivel: {reset}  {naranja}{self.nivel}{reset}' +
            f'\nBolsa:   {cyan}{len(self.bolsa)}{reset}' + ' palabras restantes.'
            f'\n{bold}{verde}Palabras acertadas: ({len(self.acertadas)}){reset} {self.acertadas}' +
            f'\n{bold}{rojo}Palabras erradas:   ({len(self.erradas)}) {reset}{self.erradas}\n'
        )        
        return txt

    def calcular_nivel(self):
        total_acertadas = len(self.acertadas)
        total_erradas = len(self.erradas)
        total_bolsa = len(self.bolsa)

        if total_bolsa == 0 and total_erradas == 0:
            return 5

        porcentaje_acertadas = (total_acertadas / (total_bolsa + total_erradas)) * 100

        if porcentaje_acertadas >= 80:
            return 5
        elif porcentaje_acertadas >= 60:
            return 4
        elif porcentaje_acertadas >= 40:
            return 3
        elif porcentaje_acertadas >= 20:
            return 2
        else:
            return 1

def login():
    while True:
        player = input('Nombre: ').strip().lower()
        archivo_jugador = f'{player}.pkl'

        if path.exists(archivo_jugador):
            with open(archivo_jugador, 'rb') as file:
                jugador = pickle.load(file)

            for intento in range(3):
                clave = getpass.getpass('Clave: ').strip()
                if jugador.clave != clave:
                    intentos_restantes = 2 - intento
                    print(
                        f'{rojo}\nClave incorrecta para el nombre ingresado.{reset}'
                        f'\nIntentos restantes: {intentos_restantes}\n'
                    )
                else:
                    return jugador, player

            print(f'{rojo}Has excedido el número máximo de intentos.{reset}\n')
            continue

        else:
            print(f'{cursiva}{amarillo}Jugador no encontrado.\nSe ha creado un nuevo registro para {reset}{verde}{bold}{player}{reset}.\n')
            clave = getpass.getpass('Clave: ').strip()
            jugador = Jugador(player, clave)

            with open(archivo_jugador, 'wb') as archivo:
                pickle.dump(jugador, archivo)

            return jugador, player

jugador, player = login()

acertadas = jugador.acertadas
erradas = jugador.erradas
bolsa = jugador.bolsa

print(jugador)


def salir():
    with open(f'{player}.pkl', 'wb') as archivo:
        pickle.dump(jugador, archivo)
    print(jugador)
    sys.exit()


def ingreso():
    while True:
        intentada = input('\nIngresá una palabra de 5 letras: ').strip().lower()
        if len(intentada) != 5 and intentada != 'x':
            print(f'\nLa palabra debe ser de {bold}{verde}CINCO{reset} letras.\nProbá de nuevo.')
        elif intentada == 'x':
            print('\nPrograma interrumpido.\Saliendo.\n')
            jugador.erradas.append(palabra_secreta)
            salir()
        elif intentada not in bolsa and intentada != palabra_secreta:
        	print('\nLa palabra no está en la base de datos.\nIntentá otra vez.')
        else:
            return intentada

def intento(intentada, palabra_secreta):
    resultado = []
    for i, letra in enumerate(intentada):
        if letra == palabra_secreta[i]:
            resultado.append('🟢')  # Correcto
        elif letra in palabra_secreta:
            resultado.append('🟡')  # En la palabra pero en posición incorrecta
        else:
            resultado.append('🔴')  # Incorrecto
    return resultado  # Devuelve la lista en lugar de la cadena

# Límite de intentos
limite_intentos = 6 - jugador.nivel

# Ciclo del juego
while True:
    if not bolsa:
        # Si la bolsa quedó vacía, recargar desde archivo (opcional) o salir.
        bolsa = cargar_bolsa()
        if not bolsa:
            print(f'{rojo}No quedan palabras disponibles. Saliendo.{reset}')
            sys.exit()

    palabra_secreta = random.choice(list(bolsa))
    #print(f'Palabra secreta: {palabra_secreta}')  # Para depuración
    bolsa.remove(palabra_secreta)

    print(f'{bold}\nWORDLE{reset} de 5 letras.\nTenés {limite_intentos} intentos.\n\n{naranja}Ingresá una {bold} X {reset}{naranja} en cualquier momento para salir.{reset} \n{blanco}¡¡La {reset}{bold}Ñ{reset}{blanco} también existe!!{reset}\n\n🟢 {verde}letra correcta en la posición correcta\n🟡 {amarillo}letra correcta en la posición equivocada\n🔴 {rojo}la letra no está en la palabra.{reset}\n')
    print(len(bolsa) + 1, f'palabras posibles.\n{bold}¡¡MUCHA SUERTE!!{reset}')

    intentos = 0
    while intentos < limite_intentos:
        palabra_adivinada = ingreso()
        intentos += 1
        print(limite_intentos - intentos, 'intentos restantes...\n')
        resultado = intento(palabra_adivinada, palabra_secreta)
        print(f"Resultado: {''.join(resultado)}")

        if resultado == ['🟢'] *5:
            jugador.acertadas.append(palabra_secreta)
            jugador.nivel = jugador.calcular_nivel()
            print(f'\n 🎊 {bold}{verde}¡¡¡FELICITACIONES!!!{reset} 🎊')
            break
    else:
        jugador.erradas.append(palabra_secreta)
        jugador.nivel = jugador.calcular_nivel()

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
