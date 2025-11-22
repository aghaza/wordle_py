'''	Archivo generador de base de palabras para WORDLE. 
	Se solicitará ingresar el nombre del archivo fuente.

	El criterio es seleccionar solamente las palabras de 5 caracteres de extensión de dicha fuente. 
	Luego convertir todas las palabras resultantes a minúsculas. 
	Se quitan los caracteres y cadenas de la tupla 'quitar'. 
	Se quitan los caracteres acentuados. 
	Se convierte la lista 'bolsa' a conjunto para eliminar duplicados. 
	Se guarda el set en el archivo binario 'bolsa.pkl' que luego se intentará recuperar desde main.py 
	Se muestra en pantalla la cantidad de palabras generadas. 

    Creado por George Aghazarian - aghazarian@pm.me
    Última versión: 21 de noviembre de 2025 - 15:20

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
import pickle
import sys
if system("clear") != 0: system("cls")  # Limpiar pantalla

nombre_archivo = input('Ingrese el nombre del archivo fuente para generar\nla base de palabras primaria: ')
if not path.exists(nombre_archivo):
	print('No se encuentra el archivo ingresado.')
	sys.exit()

# Abre el archivo en modo lectura
with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
    # Convierte el contenido del archivo en una lista de líneas
    palabras = archivo.read().split()

# Seleccionamos únicamente las palabras de 5 caracteres de longitud
# y las almacenamos en la lista bolsa

bolsa = []

for palabra in palabras:
    if '/' in palabra:
        palabra = palabra.split('/')[0]
# el filtro de la barra es porque hay muchas palabras que aparecen en "es.dic" con un "/" y luego más caracteres
# por ejemplo ácimo/S ácueo/SG áfilo/SG áfrico/GS        
    if len(palabra) == 5:
        bolsa.append(palabra)


# Tupla de caracteres y subcadenas a quitar
quitar = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0, '!', '@', '#', '$', '%', '^', '&', '-', '_', '.', 'ç', 'sh',':')

# Convertir a minúsculas 
bolsa = [e.lower() for e in bolsa]

# quitar las palabras que contienen caracteres/subcadenas en "quitar"
bolsa = [e for e in bolsa if not any(str(k) in e for k in quitar)]

# Convertir todos los caracteres acentuados a los mismos caracteres sin acentuar
acento = ("á", "é", "í", "ó", "ú", "ü")
cambiar = ('a', 'e', 'i', 'o', 'u', 'u')
mapa_acento = dict(zip(acento, cambiar))

def quitar_acentos(palabra):
    return ''.join(mapa_acento.get(char, char) for char in palabra)

bolsa = [quitar_acentos(e) for e in bolsa]
bolsa = set(bolsa) # convertimos la lista a conjunto para eliminar posibles duplicados

# Salvamos el set a el archivo binario "bolsa.pkl"
with open('bolsa.pkl', 'wb') as archivo:
    pickle.dump(bolsa, archivo)

# para ver todas las palabras generadas en la bolsa # # descomentar las siguientes dos líneas 
# for e in bolsa:
# 	print(e, end = '  ')
	
print(len(bolsa), 'palabras generadas disponibles.\n')
