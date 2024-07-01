import os 
from flask import Flask, send_file, render_template

app = Flask(__name__)


with app.app_context():
    from . import db
    db.init_app(app)

@app.route('/')
def hello():
    return 'Que, tal!'


@app.route('/discos')
def discos():
   
    base_de_datos = db.get_db()
    consulta = """
        SELECT a.title AS Album, ar.name AS Artista, COUNT(t.name) AS cantCanciones FROM albums a
        JOIN artists ar ON a.ArtistId = ar.ArtistId
        JOIN tracks t ON a.AlbumId = t.AlbumId
        GROUP BY a.AlbumId
        ORDER BY Album;
    """

    resultado = base_de_datos.execute(consulta)
    lista_de_resultados = resultado.fetchall()
    return render_template("discos.html", discos=lista_de_resultados)


@app.route('/canciones')
def canciones():
    base_de_datos = db.get_db()
    consulta = """
        SELECT name FROM tracks
        ORDER BY name;
    """

    resultado = base_de_datos.execute(consulta)
    lista_de_resultados = resultado.fetchall()
    return render_template("cancion.html", canciones=lista_de_resultados)


@app.route('/Artista')
def artista():
   
    base_de_datos = db.get_db()
    consulta = """
        SELECT  ar.name AS Artista FROM artists ar
        ORDER BY Artista;
    """

    resultado = base_de_datos.execute(consulta)
    lista_de_resultados = resultado.fetchall()
    return render_template("artistas.html", artista=lista_de_resultados)


@app.route('/favicon.ico')
def favicon():
    return send_file('static/flavicon.ico')