''' Programa para recibir sugerencias de nuevas palabras por parte de los usuarios.
	Generará un archivo <sugerencias_{fecha_y_hora}.log> solamente en el caso
	que el usuario haya generado nuevas palabras válidas.
	
	El código no admitirá nuevas palabras que no estén dentro del patrón que solamente
	incluye: mayúsculas y minúsculas incluida la "Ñ ñ", vocales con tíldes o "Ü ü".

    Este programa es un accesorio complementario.

    Creado por George Aghazarian - aghazarian@pm.me
    Última versión: 25 de noviembre de 2025 - 21:00

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
        agregador_web.py        - igual a agregador.py pero con gestión en GitHub.
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
import re
from datetime import datetime

# Estilos de texto
bold  = "\033[1m"
reset = "\033[0m"
cursiva = "\033[3m"

# Colores de texto
verde = "\033[32m"
rojo  = "\033[31m"
naranja = "\033[38;5;214m"
cyan = "\033[36m"          # Cyan
azul_brillante = "\033[94m"


def ingreso(nuevas = None):
	if nuevas == None:
		nuevas = []
	patron = r'^[a-zA-ZáéíóúÁÉÍÓÚüÜñÑ]+$'
	print(f"{naranja}Ingrese una {bold}X{reset} {naranja}en cualqier momento para salir.{reset}\n")
	sugerencia = input("Palabra a sugerir: ").strip().lower()
	if sugerencia == "x":
		return nuevas
	elif len(sugerencia) != 5:
		print(f"\n{azul_brillante}Solo se admiten palabras de 5 caracteres.{reset}")
		return ingreso(nuevas)
	elif not re.match(patron, sugerencia):
		print("\nPalabra con caracteres no válidos")
		return ingreso(nuevas)
	else:
		nuevas.append(sugerencia)
		print(f"{verde}Palabra {bold}{sugerencia}{reset} {verde}agregada a la lista.{reset}\n")
		return ingreso(nuevas)
	return nuevas

nuevas = ingreso()

def nuevas_log(nuevas):
    fecha_hora = datetime.now().strftime("%Y%m%d_%H%M%S")
    nombre_archivo = f'sugerencias_{fecha_hora}.log'
    
    with open(nombre_archivo, 'w') as destino:
        destino.write(str(nuevas))

if len(nuevas) != 0:
	print(f"{cursiva}Guardando...{reset}")
	nuevas_log(nuevas)


print(f"\n{azul_brillante}Gracias por la colaboración.{reset}\n")
print("Colaboraste con", len(nuevas), "palabras.")
print("Palabras que aportaste: " , nuevas)

