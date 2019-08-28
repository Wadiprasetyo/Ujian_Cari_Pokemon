from flask import Flask, render_template, redirect, request, url_for, abort
import requests

app = Flask(__name__)

#home
@app.route('/')
def home():
    return render_template('home.html')

#pencarian pokemon
@app.route('/post', methods=['POST'])
def search():
    nama = request.form['nama']
    return redirect(url_for('hasil', nama=nama))

#menampilkan pencarian dari route di atas
@app.route('/hasil/<string:nama>')
def hasil(nama):
    PokemonName = nama.lower()
    url = 'https://pokeapi.co/api/v2/pokemon/'+PokemonName
    pokemon = requests.get(url)
    if str(pokemon) == '<Response [404]>':
        abort(404)
    else:
        return render_template('hasil.html', pokemon=pokemon)

#error
@app.errorhandler(404)
def error(error):
    return render_template('error.html')

if __name__ == "__main__":
    app.run(debug=True)