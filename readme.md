    *WORDLE* python.

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
        sugerencias.py				- receptor de sugerencias de palabras
        conversor.py    		- convierte bolsa.pkl a bolsa_set.py cuyo contenido es bolsa = {aquí dentro un set con las palabras}
        list2bin.py					- proceso iverso a conversor.py
        wordsJS_to_pyPKL.py		- igual a list2bin.py pero a partir de words.js
        bolsaPKL_to_wordsJS.py	- proceso inverso a wordsJS_to_pyPKL.py
        words.js				- FUENTE ÚNICA de palabras: set de 1012 palabras de 5 letras, sin repetidos,
                                  idéntica a la del repo webwordle (versión web en https://aghaza.github.io/webwordle/)
        frecuentes.txt  		- base de las palabras más frecuentes del castellano
        es.dic          		- corrector ortográfico de LibreOffice para usar de base de miles de plabras
        icono.png       		- icono de WORDLE

    La versión web usa exactamente el mismo words.js: para actualizar el diccionario hay que editarlo
    y regenerar bolsa.pkl con wordsJS_to_pyPKL.py (start.sh lo hace solo si falta).

    Requiere python3
