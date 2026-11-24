#!/bin/bash
cd "$(dirname "$0")"
# Regenera la bolsa desde la fuente unica (words.js) si no existe
[ -f bolsa.pkl ] || python3 wordsJS_to_pyPKL.py
python3 main.py
