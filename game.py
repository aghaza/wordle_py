from flask import Flask, request, render_template
import random

app = Flask(__name__)

# Configuración de estilo y colores (sin cambios)

# Conjunto de palabras
bolsa = {'adobe', 'banco', 'tensa', 'muslo', 'decia', 'final', 'puedo', 'nieto', 'panza', 'amago', 'falsa', 'algun', 'pesto', 'palco', 'galgo', 'globo', 'marte', 'robar', 'amado', 'pasto', 'valga', 'pujar', 'fleje', 'queso', 'corso', 'nogal', 'zorra', 'costo', 'lamer', 'mixto', 'sarta', 'salmo', 'casco', 'claro', 'denso', 'monja', 'solas', 'barco', 'cebra', 'tipos', 'logro', 'medir', 'dicen', 'avion', 'menor', 'buche', 'aquel', 'ameba', 'niñas', 'forro', 'ducha', 'rifar', 'viuda', 'plaga', 'zueco', 'hueso', 'covid', 'hacer', 'bolso', 'obeso', 'sucio', 'metro', 'prado', 'puede', 'resto', 'humor', 'arabe', 'renal', 'datil', 'balsa', 'pauta', 'viene', 'hasta', 'siete', 'deuda', 'lista', 'quema', 'rodar', 'lopez', 'ojera', 'ambos', 'prole', 'burro', 'coati', 'causa', 'moral', 'cuero', 'sabio', 'cheto', 'nivel', 'trama', 'cobra', 'troja', 'ingle', 'jalar', 'nuevo', 'yacer', 'lanza', 'momia', 'novio', 'libre', 'rodeo', 'virus', 'pesar', 'oruga', 'dardo', 'salsa', 'jamon', 'seran', 'rehen', 'donde', 'omega', 'choza', 'amiga', 'rollo', 'quita', 'toser', 'mambo', 'hondo', 'magma', 'casto', 'plaza', 'pulpa', 'sazon', 'vasco', 'irani', 'vuelo', 'fuera', 'aroma', 'estos', 'sumas', 'bolsa', 'trato', 'mundo', 'yerba', 'clase', 'oreja', 'reino', 'pausa', 'cueca', 'oveja', 'cenar', 'habla', 'cosas', 'lindo', 'julio', 'pinta', 'joven', 'lapiz', 'vetar', 'mirlo', 'paris', 'pajar', 'corto', 'cobro', 'tapon', 'hecho', 'sidra', 'estoy', 'envio', 'rumbo', 'friso', 'razon', 'epoca', 'hiato', 'susto', 'lacra', 'macro', 'licor', 'regir', 'dueto', 'quedo', 'ataud', 'piñon', 'mucho', 'diosa', 'suave', 'lerdo', 'votar', 'simio', 'manca', 'fatal', 'volar', 'silla', 'palma', 'demas', 'pucho', 'cruel', 'polen', 'santa', 'crema', 'censo', 'motor', 'sigue', 'grano', 'icono', 'cerca', 'pleno', 'reñir', 'nueva', 'amigo', 'manos', 'somos', 'animo', 'atril', 'junco', 'ahora', 'cargo', 'falta', 'norte', 'atras', 'zorro', 'gasto', 'tibio', 'medio', 'peaje', 'todos', 'lejos', 'llaga', 'carga', 'dudar', 'halar', 'monje', 'bosta', 'presa', 'ellas', 'judio', 'tenga', 'colar', 'ligar', 'agudo', 'pizca', 'hotel', 'gofio', 'debut', 'mucha', 'honda', 'cante', 'ardor', 'droga', 'vasca', 'debil', 'domar', 'podia', 'rotor', 'potro', 'caldo', 'rodea', 'bajon', 'sobre', 'llave', 'mutar', 'facil', 'visar', 'agora', 'senil', 'bardo', 'gallo', 'lucro', 'muere', 'fluir', 'venta', 'jamas', 'vigor', 'vamos', 'plazo', 'poner', 'temer', 'hemos', 'mismo', 'matiz', 'huron', 'lloro', 'etica', 'quiza', 'ostia', 'obras', 'niños', 'podar', 'botar', 'junto', 'setas', 'horca', 'vende', 'saber', 'graso', 'conde', 'terco', 'perro', 'cromo', 'disco', 'daban', 'equis', 'ciego', 'viejo', 'dueña', 'letra', 'fluor', 'tenia', 'fuego', 'cañon', 'damos', 'calva', 'trigo', 'labor', 'podra', 'grado', 'carpa', 'unico', 'bayas', 'yuyos', 'polvo', 'forma', 'conga', 'pubis', 'vista', 'pasos', 'mates', 'nunca', 'teson', 'largo', 'terca', 'mareo', 'sauce', 'plano', 'cobre', 'negro', 'punto', 'molar', 'selva', 'gamba', 'lenta', 'gesta', 'calvo', 'corte', 'cinto', 'salva', 'andar', 'miles', 'ronco', 'desde', 'jueza', 'ellos', 'calza', 'flota', 'bella', 'brujo', 'leche', 'polca', 'polar', 'audio', 'toque', 'bueno', 'ufano', 'vendo', 'tosco', 'dulce', 'termo', 'mecha', 'golpe', 'santo', 'lider', 'sacro', 'herir', 'marea', 'otros', 'pedir', 'tacha', 'grifa', 'segun', 'darse', 'pocos', 'latex', 'pieza', 'tales', 'fumar', 'zurdo', 'panel', 'llego', 'cinta', 'vapor', 'islas', 'circo', 'secar', 'helar', 'nasal', 'pique', 'soplo', 'tordo', 'pasta', 'yendo', 'valor', 'dejar', 'pañal', 'llano', 'monte', 'buque', 'talla', 'paria', 'palmo', 'vetos', 'puñal', 'pesos', 'algas', 'dolor', 'merca', 'plena', 'flaca', 'salir', 'feliz', 'bazar', 'rotar', 'facho', 'sitio', 'fresa', 'viudo', 'corno', 'enojo', 'vaina', 'regla', 'otoño', 'venir', 'guita', 'novia', 'linda', 'tanta', 'cueva', 'tigre', 'saten', 'breve', 'soñar', 'temas', 'brasa', 'linea', 'oxido', 'arder', 'credo', 'grave', 'amada', 'bondi', 'zurda', 'cinco', 'axial', 'habra', 'cesto', 'natal', 'secta', 'nevar', 'dalia', 'triza', 'crear', 'culto', 'clima', 'plana', 'horas', 'lacio', 'golfo', 'miron', 'brazo', 'vulva', 'suela', 'ceder', 'calma', 'china', 'autor', 'frita', 'cloro', 'sueño', 'traer', 'sexto', 'rayar', 'deseo', 'lunes', 'feroz', 'canta', 'vocal', 'trola', 'fugaz', 'texto', 'harto', 'civil', 'lirio', 'dueño', 'urgir', 'dicho', 'larga', 'foton', 'yogur', 'vieja', 'secas', 'papel', 'cifra', 'grasa', 'grapa', 'tigra', 'deudo', 'serie', 'chica', 'jarro', 'salar', 'murga', 'molde', 'salud', 'rozar', 'tomar', 'canon', 'mitad', 'tiesa', 'pobre', 'merma', 'fusta', 'muela', 'grupo', 'manso', 'nacer', 'callo', 'salon', 'grupa', 'guion', 'sordo', 'comun', 'brete', 'union', 'tenis', 'total', 'delta', 'ganar', 'mando', 'grifo', 'limon', 'rizar', 'juego', 'pulga', 'obvio', 'legar', 'sutil', 'bañar', 'latir', 'musgo', 'señor', 'local', 'lleva', 'listo', 'mujer', 'sorbo', 'purga', 'igneo', 'suele', 'tiene', 'pista', 'nadie', 'chile', 'cerro', 'labra', 'diera', 'surco', 'garza', 'tacho', 'menos', 'panal', 'liana', 'enema', 'jaque', 'armar', 'campo', 'vacio', 'palpa', 'cupon', 'cielo', 'tener', 'joder', 'armas', 'aldea', 'antes', 'capaz', 'aviar', 'grita', 'haber', 'estas', 'mamut', 'tonto', 'torno', 'islam', 'abril', 'llega', 'llama', 'pulir', 'arete', 'motel', 'danza', 'cacho', 'ayuda', 'fonda', 'secos', 'morir', 'dogma', 'gripe', 'hijos', 'serio', 'busca', 'perno', 'greda', 'pasar', 'estan', 'suelo', 'cajon', 'maula', 'vayan', 'debia', 'color', 'queda', 'sabia', 'pared', 'fiera', 'cardo', 'males', 'unica', 'opalo', 'salto', 'mayor', 'ebrio', 'jorge', 'naipe', 'grada', 'naval', 'cerdo', 'trece', 'arreo', 'freno', 'trata', 'posar', 'rumba', 'exito', 'pilar', 'extra', 'tonta', 'flojo', 'fiado', 'samba', 'raton', 'barba', 'parir', 'ojala', 'bruma', 'harta', 'pueda', 'sable', 'garra', 'ciega', 'rubia', 'tinta', 'poder', 'tallo', 'vodka', 'fibra', 'cuela', 'adobo', 'madre', 'patio', 'luego', 'verde', 'calor', 'grito', 'valgo', 'piden', 'sumar', 'bello', 'favor', 'vivir', 'beber', 'abaco', 'tumbo', 'judia', 'trozo', 'rosas', 'cande', 'calco', 'chico', 'floja', 'navio', 'tanza', 'creer', 'llora', 'marco', 'villa', 'meter', 'meses', 'pario', 'pezon', 'otras', 'drama', 'birra', 'karma', 'aguja', 'mente', 'dorso', 'coñac', 'liceo', 'gramo', 'ovino', 'junio', 'fecha', 'casta', 'tarea', 'huevo', 'doble', 'gatos', 'curry', 'tarro', 'fango', 'rifle', 'placa', 'papal', 'brisa', 'lente', 'media', 'guiso', 'huida', 'tenso', 'malva', 'larva', 'falso', 'lavar', 'nieta', 'tengo', 'valle', 'ganso', 'teñir', 'bledo', 'dupla', 'seria', 'senda', 'piton', 'totem', 'noche', 'manco', 'varon', 'urano', 'fondo', 'fosil', 'ramal', 'nalga', 'comer', 'ciclo', 'pollo', 'berro', 'sobar', 'mejor', 'tapia', 'truco', 'sorda', 'velon', 'calle', 'ojear', 'tecla', 'sonar', 'leona', 'usted', 'orden', 'digan', 'heder', 'jaula', 'burla', 'matar', 'pinza', 'besar', 'aguda', 'edema', 'horno', 'curso', 'vivaz', 'frito', 'entre', 'misma', 'nadar', 'trino', 'sesgo', 'cerco', 'ideas', 'caliz', 'libro', 'hacen', 'veloz', 'saldo', 'potra', 'mirar', 'broma', 'justa', 'oblea', 'hacia', 'raudo', 'hedor', 'miedo', 'estar', 'moler', 'pixel', 'pinto', 'nueve', 'becar', 'viaje', 'busco', 'solos', 'tipeo', 'sexta', 'freir', 'azote', 'bollo', 'abeja', 'bruja', 'oculo', 'aromo', 'tarde', 'radio', 'prisa', 'indio', 'costa', 'calar', 'calce', 'viste', 'tumba', 'tilde', 'turco', 'bagre', 'micro', 'malta', 'litro', 'talar', 'tanto', 'horma', 'sarro', 'reloj', 'apoyo', 'ambar', 'habia', 'lleno', 'drupa', 'colmo', 'ñandu', 'sacra', 'reten', 'cedro', 'etapa', 'tango', 'ladra', 'mosca', 'polla', 'flaco', 'lucha', 'plato', 'carne', 'vuela', 'vello', 'donar', 'fuste', 'zamba', 'tamiz', 'parto', 'nariz', 'burdo', 'siglo', 'maria', 'peste', 'casos', 'tarta', 'pablo', 'buena', 'canto', 'llena', 'ronda', 'igual', 'torta', 'persa', 'visto', 'rolar', 'lucir', 'parte', 'tinto', 'decir', 'atroz', 'veces', 'gente', 'mutuo', 'punta', 'peral', 'justo', 'jarra', 'silba', 'copar', 'zonas', 'mudar', 'frote', 'norma', 'diana', 'tapiz', 'padre', 'marzo', 'deben', 'morsa', 'fiero', 'limbo', 'mango', 'caoba', 'curva', 'pardo', 'cavar', 'lento', 'mutua', 'sanar', 'balde', 'corea', 'morro', 'ojota', 'tieso', 'adios', 'banda', 'lugar', 'coima', 'resta', 'india', 'malla', 'nicho', 'libra', 'enero', 'timar', 'boina', 'jugar', 'calmo', 'sacar', 'ovalo', 'tirar', 'burda', 'marca', 'datos', 'varar', 'barro', 'sedar', 'rubio', 'parda', 'nieve', 'plata', 'arbol', 'trolo', 'preso', 'boldo', 'todas', 'carta', 'basta', 'fauna', 'bulto', 'arroz', 'trote', 'trono', 'mamar', 'burra', 'quien', 'laton', 'tambo', 'reojo'}
acertadas = []
erradas = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    palabra_secreta = random.choice(list(bolsa))
    bolsa.remove(palabra_secreta)
    
    intentada = request.form['intentada'].strip().lower()
    
    if len(intentada) != 5 and intentada != 'x':
        return f'La palabra debe ser de CINCO letras. Probá de nuevo.'

    elif intentada not in bolsa and intentada != palabra_secreta:
        return 'La palabra no está en la base de datos. Intentá otra vez.'
    
    resultado = intento(intentada, palabra_secreta)
    
    if resultado == ['🟢'] * 5:
        acertadas.append(palabra_secreta)
        return '🎊 ¡¡¡FELICITACIONES!!! 🎊'
        
    else:
        erradas.append(palabra_secreta)
        return f'🔥 CAGASTE FUEGO 🔥 La palabra era: {palabra_secreta.upper()}'

def intento(intentada, palabra_secreta):
    resultado = []
    for i, letra in enumerate(intentada):
        if letra == palabra_secreta[i]:
            resultado.append('🟢')  
        elif letra in palabra_secreta:
            resultado.append('🟡')
        else:
            resultado.append('🔴')  
    return resultado  

if __name__ == '__main__':
    app.run(debug=True)
