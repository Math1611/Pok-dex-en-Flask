from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# Base de datos ficticia de Pokémon 
pokedex = [
   {"id": 1, "nombre": "Bulbasaur", "tipo": "Planta/Veneno", "imagen": "bulbasaur.png", "poder": 45, "altura": "0.7m", "peso": "6.9kg"},
   {"id": 4, "nombre": "Charmander", "tipo": "Fuego", "imagen": "charmander.png", "poder": 39, "altura": "0.6m", "peso": "8.5kg"},
   {"id": 7, "nombre": "Squirtle", "tipo": "Agua", "imagen": "squirtle.png", "poder": 44, "altura": "0.5m", "peso": "9.0kg"},
   {"id": 25, "nombre": "Pikachu", "tipo": "Eléctrico", "imagen": "pikachu.png", "poder": 35, "altura": "0.4m", "peso": "6.0kg"},
   {"id": 39, "nombre": "Jigglypuff", "tipo": "Normal/Hada", "imagen": "jigglypuff.png", "poder": 115, "altura": "0.5m", "peso": "5.5kg"},
   {"id": 52, "nombre": "Meowth", "tipo": "Normal", "imagen": "meowth.png", "poder": 40, "altura": "0.4m", "peso": "4.2kg"},
   {"id": 54, "nombre": "Psyduck", "tipo": "Agua", "imagen": "psyduck.png", "poder": 50, "altura": "0.8m", "peso": "19.6kg"},
   {"id": 94, "nombre": "Gengar", "tipo": "Fantasma/Veneno", "imagen": "gengar.png", "poder": 60, "altura": "1.5m", "peso": "40.5kg"},
   {"id": 95, "nombre": "Onix", "tipo": "Roca/Tierra", "imagen": "onix.png", "poder": 35, "altura": "8.8m", "peso": "210.0kg"},
   {"id": 143, "nombre": "Snorlax", "tipo": "Normal", "imagen": "snorlax.png", "poder": 160, "altura": "2.1m", "peso": "460.0kg"}
]


def pokemon_no_encontrado(mensaje: str):
    return render_template('404.html', mensaje=mensaje), 404

@app.route('/')
def index():
    return redirect(url_for('mostrar_pokemon'))

@app.route('/pokemon')
def mostrar_pokemon():
    return render_template('pokemon.html', pokedex=pokedex)

@app.route('/pokemon/cantidad/<int:cantidad>')
def mostrar_cantidad(cantidad):
    cantidad = max(0, min(cantidad, len(pokedex)))
    subset = pokedex[:cantidad]
    return render_template('pokemon.html', pokedex=subset)

@app.route('/pokemon/<identificador>')
def mostrar_detalle(identificador):
    encontrado = None
    if identificador.isdigit():
        numero = int(identificador)
        for p in pokedex:
            if p.get('id') == numero:
                encontrado = p
                break
    else:
        nombre_buscar = identificador.replace('-', ' ').strip().lower()
        for p in pokedex:
            if p.get('nombre', '').lower() == nombre_buscar:
                encontrado = p
                break

    if not encontrado:
        mensaje = f'No pudimos encontrar nada sobre "{identificador}" en la pokedex'
        return pokemon_no_encontrado(mensaje)
    return render_template('pokemon.html', pokedex=[encontrado])

if __name__ == '__main__':
    app.run(debug=True)