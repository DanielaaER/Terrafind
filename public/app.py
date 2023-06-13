from flask import Flask, request
from flask_cors import CORS

import pandas as pd
import folium

app = Flask(__name__)
CORS(app)

@app.route('/buscar', methods=['POST'])
def ejecutar_python():
    municipios_mostrar = request.json['municipios_mostrar']
    # Ejecuta el archivo de Python utilizando el intérprete de Python
    # Cargar datos del CSV
    municipios_csv = "municipios.csv"
    municipios = pd.read_csv(municipios_csv)


    # Filtrar los datos de los municipios a mostrar
    municipios_filtrados = pd.DataFrame()

    for municipio in municipios_mostrar:
        municipios_temp = municipios[municipios['NOM_ENT'] == municipio].head(1)

       
        if municipios_temp.empty:
            municipios_temp = municipios[municipios['NOM_MUN'] == municipio].head(1)

        municipios_filtrados = pd.concat([municipios_filtrados, municipios_temp])
    # Crear mapa centrado en México
    mexico_map = folium.Map(location=[23.626672, -102.537292], zoom_start=5, dragging=False)

    # Agregar marcadores de cada municipio al mapa
    for index, row in municipios_filtrados.iterrows():
        lat = row['LAT_DEC']
        lon = row['LON_DEC']
        estado = row['NOM_ENT']
        tooltip = f"{estado}"
        marker = folium.Marker(location=[lat, lon], tooltip=tooltip)
        marker.add_to(mexico_map)

   

    # Mostrar mapa
    mexico_map.save("search.html")
    respuesta = {
        'mensaje': 'Procesamiento exitoso',
        'municipios_mostrar': municipios_mostrar,
        'resultado': 'Resultado del procesamiento'
    }

    return respuesta


@app.route('/ruta', methods=['POST'])
def ruta():
    municipios_mostrar = request.json['municipios_mostrar']
    # Ejecuta el archivo de Python utilizando el intérprete de Python
    # Cargar datos del CSV
    print(municipios_mostrar)
    municipios_csv = "municipios.csv"
    municipios = pd.read_csv(municipios_csv)


    # Filtrar los datos de los municipios a mostrar
    municipios_filtrados = pd.DataFrame()

    for municipio in municipios_mostrar:
        municipios_temp = municipios[municipios['NOM_ENT'] == municipio].head(1)
       
        if municipios_temp.empty:
            municipios_temp = municipios[municipios['NOM_MUN'] == municipio].head(1)

        municipios_filtrados = pd.concat([municipios_filtrados, municipios_temp])
        
        print(municipios_temp)
    # Crear mapa centrado en México
    
    mexico_map = folium.Map(location=[23.626672, -102.537292], zoom_start=5, dragging=False)

    # Agregar marcadores de cada municipio al mapa
    for index, row in municipios_filtrados.iterrows():
        lat = row['LAT_DEC']
        lon = row['LON_DEC']
        estado = row['NOM_ENT']
        tooltip = f"{estado}"
        marker = folium.Marker(location=[lat, lon], tooltip=tooltip)
        marker.add_to(mexico_map)

   

    # Agregar la línea que une los marcadores
    ruta_coords = []
    for municipio in municipios_mostrar:
        print(municipio)
        coords = municipios_filtrados[(municipios_filtrados['NOM_MUN'] == municipio) | (municipios_filtrados['NOM_ENT'] == municipio)][['LAT_DEC', 'LON_DEC']].values.tolist()[0]

        print(coords)
        ruta_coords.append(coords)
    folium.PolyLine(locations=ruta_coords, color='blue', weight=3).add_to(mexico_map)

    # Mostrar mapa
    mexico_map.save("route.html")
    respuesta = {
        'mensaje': 'Procesamiento exitoso',
        'municipios_mostrar': municipios_mostrar,
        'resultado': 'Resultado del procesamiento'
    }

    return respuesta

if __name__ == '__main__':
    app.run()
