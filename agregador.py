''' Programa para agregar, eliminar, contabilizar y listar las palabras de la base de datos para el juego WORDLE.
    Buscará la base de palabras en "words.js" o en el binario "bolsa.pkl", en caso de no encontrarla intentará 
    reconstruirla mediante generador.py y si no se encontrara este generará un conjunto de palabras
    vacío que podrá ser llenado con este mismo agregador.
    
    Además de modificar <bolsa.pkl> generará una versión <words.js> mediante el conversor <bolsaPKL_to_wordsJS.py>
    para utilizar en la versión web.
    
    En el caso de agregarse palabras nuevas generará un archivo de registro llamado nuevas.log
    cuyo contenido será una lista [palabra_nueva1, palabra_nueva2, ... ,palabra_nuevaN]

    En el caso de eliminarse palabras generará un archivo de registro llamado elim.log
    cuyo contenido será una lista [palabra_eliminada1, palabra_eliminada2, ... ,palabra_eliminadaN]

    En cualquiera de estos casos (tanto se agreguen o se quiten palabras) si ya existieran registros previos
    de los archivos .log su contenido se incrementará con los nuevos registros.

    Creado por George Aghazarian - aghazarian@pm.me
    Última versión: 21 de noviembre de 2025 - 18:28

    Este programa es un accesorio complementario.

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
import subprocess
import pickle
import sys
import ast

# Estilos de texto
bold  = "\033[1m"
reset = "\033[0m"

# Colores de texto
verde = "\033[32m"
rojo  = "\033[31m"
naranja = "\033[38;5;214m"
cyan = "\033[36m"          # Cyan
azul_brillante = "\033[94m"

def js2bin():
		
	if path.exists('words.js'):
		with open('words.js', 'r') as file:
			print(f"Archivo {bold}{verde}<words.js>{reset} encontrado.\nSe usará como base y se generará {bold}{verde}<bolsa.pkl>{reset} a partir del mismo.\n")
			for line in file:
				if line.startswith("const WORDS = "):
					# Extraer el contenido de const WORDS = []
					bolsa_content = line.split("= ", 1)[1].strip().rstrip(';')  # Eliminar el punto y coma
					# Evaluar la expresión
					bolsa = set(ast.literal_eval(bolsa_content.strip('[]')))
	else:
		print(f"No se encuentra el archvo {bold}{verde}<words.js>{reset}.\nSe usará {bold}{verde}<bolsa.pkl>{reset} como base.\n")
		return None

	with open('bolsa.pkl', 'wb') as archivo:
		pickle.dump(bolsa, archivo)

print(f"Verificando existencia de {bold}<words.js>{reset}...")
js2bin()

nuevas = 0
eliminadas = 0

if path.exists('nuevas.log'):
    with open('nuevas.log', 'r') as file:
        nuev = file.read()
        nuev = ast.literal_eval(nuev)
    print(f'Las últimas palabras agregadas son:\n{nuev}\n')
else:
    nuev = []

if path.exists('elim.log'):
    with open('elim.log', 'r') as file:
        elim = file.read()
        elim = ast.literal_eval(elim)
    print(f'Las últimas palabras eliminadas son:\n{elim}\n')

else:
    elim = []

def guardar():
    global bolsa
    with open('bolsa.pkl', 'wb') as archivo:
        pickle.dump(bolsa, archivo)
    if path.exists("bolsaPKL_to_wordsJS.py"):
        subprocess.run(['python3', 'bolsaPKL_to_wordsJS.py'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    else:
        print(f"{rojo}No se ha podido generar <words.js> porque no se ha encontrado el conversor {bold}<bolsaPKL_to_wordsJS.py>.{reset}")

def nuevas_log():
	destino = open('nuevas.log', 'w')
	destino.write(str(nuev))
	destino.close()

def elim_log():
	destino = open('elim.log', 'w')
	destino.write(str(elim))
	destino.close()		

def salida():
    if nuevas > 0:
        print(f'\nSe han agregado las siguientes palabras nuevas ({verde}{nuevas}{reset}):')
        print(nuev)
        nuevas_log()
        
    if eliminadas > 0:
        print(f'\nSe han eliminado las siguientes palabras de la base ({rojo}{eliminadas}{reset}):')
        print(elim)
        elim_log()
        
    print(f'\n{azul_brillante}Cantidad de palabras actual:{reset}', len(bolsa), f'{azul_brillante}palabras.{reset}\n')
    
    if path.exists("bolsaPKL_to_wordsJS.py"):
        print(f"{verde}Se ha generado {bold}<words.js>{reset}{verde} correctamente.{reset}\n")
        subprocess.run(['python3', 'bolsaPKL_to_wordsJS.py'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    else:
        print(f"{rojo}No se ha podido generar <words.js> porque no se ha encontrado el conversor {bold}<bolsaPKL_to_wordsJS.py>.{reset}\n")
	
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
        print(f'{verde}Generador encontrado, base de datos reconstruida.{reset}\n')
        guardar()
    except subprocess.CalledProcessError:  # Solo captura la excepción sin imprimirla
        print(f'{rojo}No se ha encontrado el generador de palabras.\nSe ha creado una base de palabras vacía.\n')
        bolsa = set()
        guardar()
        
print(f'{azul_brillante}Cantidad de palabras actual:{reset}', len(bolsa), f'{azul_brillante}palabras.{reset}')
print(f'\nIngrese{verde} {bold}X{reset} en cualquier momento para salir.\n')

def buscar():
    texto = input('\nIngrese palabra a buscar: ').strip().lower()
    if texto in bolsa:
        print(f'\n{cyan}La palabra{reset} {naranja}{texto}{reset} {cyan}ya está en la base de palabras.{reset}')
        eliminar(texto)
    elif texto == 'x':
        salida()
    else:
        print(f'\nLa palabra {naranja}{texto}{reset} no está en la base de palabras.')
        agregar(texto)

def agregar(texto):
    global nuevas
    global nuev
    opcion = input(f'\n{naranja}¿Desea agregarla?{reset} (S/N): ').strip().lower()
    if opcion == 's' and len(texto) == 5:
        bolsa.add(texto)
        print(f'\nLa palabra {verde}{texto}{reset} ha sido agregada a la base de palabras.')
        nuevas += 1
        nuev.append(texto)
        guardar()
        repetir()
    elif opcion == 's' and len(texto) != 5:
        print(f'\n{rojo}La palabra solo puede tener 5 letras.{reset}\nPalabra {cyan}{texto} {reset}no agregada a la base. ')
        repetir()
    elif opcion == 'x':
        salida()
    elif opcion == 'n':
        repetir()
    elif texto == 'x':
        salida()     
    else:
        print(f'\n{rojo}Ingrese solamente {bold}S{reset} {rojo} o {bold}N.{reset}')
        agregar(texto)

def eliminar(texto):
    global eliminadas
    global elim
    opcion = input(f'\n{rojo}¿Desea {bold}ELIMINAR{reset}{naranja} {texto}{reset}{rojo} de la base de palabras?{reset} (S/N) ').strip().lower()
    if opcion == 's':
        bolsa.remove(texto)
        print(f'\nLa palabra {rojo}{texto}{reset} fue eliminada de la base de palabras.')
        eliminadas += 1
        elim.append(texto)
        guardar()
        repetir()
    elif opcion == 'n':
        repetir()
    elif opcion == 'x':
        salida()
    else:
        print(f'\n{rojo}Ingrese solamente {bold}S{reset} {rojo} o {bold}N.{reset}')
        eliminar(texto)   

def repetir():
    otra = input(f'\n{verde}¿Buscar otra palabra?{reset} (S/N): ').strip().lower()
    if otra == 's':
        buscar()
    elif otra == 'n':
        listar()
    elif otra == 'x':
        salida()    
    else:
        print(f'\n{rojo}Ingrese solamente {bold}S{reset} {rojo} o {bold}N.{reset}')
        repetir()

def listar():
    opcion = input('\n¿Listar todas las palabras disponibles? (S/N) ').strip().lower()
    if opcion == 's':
        print('\n')
        for _ in bolsa:
            print(_, end = '  ')
        print('\n')
        guardar()
        salida()
    elif opcion == 'n':
        salida()
        guardar()
    elif opcion == 'x':
        salida()
    else:
        print(f'\n{rojo}Ingrese solamente {bold}S{reset} {rojo} o {bold}N.{reset}')
        listar()       

buscar()



