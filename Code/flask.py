from flask import Flask, request, Markup
import fun_4api
import pymongo
import pandas as pd

app = Flask(__name__)


@app.route('/')
def main():
    string = """¡Bienvenido!¡Welcome!<br>Si es tu primera vez puedes encontrar toda la información sobre mi funcionamiento con la extención /help/.<br>Si no es tu primera vez, dime de que pueblo quieres que te de información, y que información deseas!!!<br> """
    return Markup(string) # string.replace('\n', '<br>')'First line.<br>Second line.<br>'

    
@app.route('/help/') 
def help():
    help_string="""Funciones disponibles:<br>
                '/pueblo?p=' : esta función permite buscar un pueblo en España y disponer de información sobre el pueblo,<br> 
                sobre su clima, la connectividad y los servicios a su alrededor.<br>
                EJEMPLO: http://127.0.0.1:5000/pueblo?p=Adanero<br>
                '/filtro?entidad=&distancia=': Nos permite detectar pueblos que esten a una distancia X de una entidad, por ejemplo un hospital.<br> 
                                                IMPORTANTE, la distancia tiene que estar en km!<br>
                EJEMPLO: http://127.0.0.1:5000/filtro?entidad=Hospital&distancia=20<br>
                """
    return help_string

@app.route('/pueblo/')
def index():
    pueblo=request.args.get('p').upper()
    folium_map=fun_4api.creacion_mapa(pueblo)
    return folium_map._repr_html_()


@app.route('/filter/')
def filter():
    cliente=pymongo.MongoClient('mongodb://localhost:27017')  # cliente , la conexion por defecto
    db=cliente.EmptiedSpain   # llamada a la base de datos
    db.emptiedSpain.create_index([('location', '2dsphere')])
    return 'Esta función aún no está disponible, esperamos tenerla disponible en cuanto antes'


if __name__ == '__main__':
    app.run(debug=False)