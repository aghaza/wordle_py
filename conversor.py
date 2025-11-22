''' Convierte el archivo binario "bolsa.pkl" a "bolsa_set.py" 
    generando un set de las palabras para manejo del programa 
    en un solo archivo.

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
import subprocess
import pickle
import sys

if path.exists('bolsa.pkl'):
    # Recuperación del archivo bolsa de palabras
    with open('bolsa.pkl', 'rb') as archivo:
        bolsa = pickle.load(archivo)
else:
    print('No está presente el archivo de la base de datos.')
    sys.exit()

bolsa = 'bolsa = ' + str(bolsa)

destino = open('bolsa_set.py', 'w')
destino.write(bolsa)
destino.close()
