''' Convierte el archivo "words.js" a "bolsa.pkl"
    generando un binario de las palabras para funcionar en "main.py"

    Creado por George Aghazarian - aghazarian@pm.me
    Última versión: 22 de noviembre de 2025 - 14:20

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
if system("clear") != 0: system("cls")  # Limpiar pantalla
import ast
import pickle
from os import system, path
import ast
import sys

if path.exists('words.js'):
    with open('words.js', 'r') as file:
        for line in file:
            if line.startswith("const WORDS = "):
                # Extraer el contenido de const WORDS = []
                bolsa_content = line.split("= ", 1)[1].strip().rstrip(';')  # Eliminar el punto y coma
                # Evaluar la expresión
                bolsa = set(ast.literal_eval(bolsa_content.strip('[]')))
else:
	print("No se encuentra el archvo <words.js>")
	sys.exit()

print(bolsa)
print(type(bolsa))
print(len(bolsa))


with open('bolsa.pkl', 'wb') as archivo:
	pickle.dump(bolsa, archivo)
    
    

