


#Se supone que este codigo es para mostrar solo los municipios que yo quiera buscar :)

import pandas as pd
import folium

def mostrar_municipios(municipios_mostrar):
    # Cargar datos del CSV
    municipios_csv = "municipios.csv"
    municipios = pd.read_csv(municipios_csv)


    # Filtrar los datos de los municipios a mostrar
    municipios_filtrados = municipios[municipios['NOM_MUN'].isin(municipios_mostrar)]

    # Crear mapa centrado en México
    mexico_map = folium.Map(location=[23.626672, -102.537292], zoom_start=5, dragging=False)

    # Agregar marcadores de cada municipio al mapa
    for index, row in municipios_filtrados.iterrows():
        lat = row['LAT_DEC']
        lon = row['LON_DEC']
        nombre = row['NOM_MUN']
        estado = row['NOM_ENT']
        tooltip = f"{nombre}, {estado}"
        marker = folium.Marker(location=[lat, lon], tooltip=tooltip)
        marker.add_to(mexico_map)

   

    # Mostrar mapa
    mexico_map.save("search.html")

# Ejemplo de uso: ingresar los municipios a mostrar como una lista al invocar la función
municipios_mostrar = ['Aguascalientes', 'Zacatecas']
mostrar_municipios(municipios_mostrar)
