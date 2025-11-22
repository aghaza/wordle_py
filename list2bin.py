''' Convierte el archivo "bolsa_set.py" a "bolsa.pkl"
    generando un binario de las palabras para funcionar en "main.py"

    Creado por George Aghazarian - aghazarian@pm.me
    Última versión: 22 de noviembre de 2025 - 15:20

    Este programa es un accesorio complementario.

    Archivos imprescindibles con al menos un jugador registrado (no se permitirán nuevos registros):
        main.py
        {player}.pkl

    Archivos imprescindibles en la carpeta si no hay jugadores registrados:
        main.py
        bolsa.pkl
    
    Archivos totales:
        main.py         	- programa principal
        generador.py    	- genera la base de palabras bolsa.pkl a partir de un archivo a elegir que contenga las palabras
        agregador.py    	- gestor del archivo bolsa.pkl que permite agregar, eliminar, contabilizar y listar las palabras
        conversor.py    	- convierte bolsa.pkl a bolsa_set.py cuyo contenido es bolsa = {aquí dentro un set con las palabras}
        list2bin.py			- proceso iverso a conversor.py
        wordsJS_to_pyPKL.py	- igual a list2bin.py pero a partir de words.js
        bolsa.pkl       	- archivo que contiene la fuente de palabras original para crear un jugador
        frecuentes.txt  	- base de las palabras más frecuentes del castellano
        es.dic          	- corrector ortográfico de LibreOfiice para usar de base de miles de plabras
        icono.png       	- icono de WORDLE

    Requiere python3

'''


from os import system, path
if system("clear") != 0: system("cls")  # Limpiar pantalla
import ast
import pickle
import sys

if path.exists('bolsa_set.py'):
    with open('bolsa_set.py', 'r') as file:
        for line in file:
            if line.startswith("bolsa = "):
                # Extraer el contenido del set
                bolsa_content = line.split("= ", 1)[1].strip()
                # Evaluar la expresión y eliminar llaves
                bolsa = set(ast.literal_eval(bolsa_content.strip('{}')))
else:
	print("No se encuentra el archvo <bolsa_set.py>")
	sys.exit()


with open('bolsa.pkl', 'wb') as archivo:
    pickle.dump(bolsa, archivo)
    
    
