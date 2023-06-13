


#Se supone que este codigo es para mostrar solo los municipios que yo quiera pero ahora los une con una linea :)
import pandas as pd
import folium

def mostrar_ruta_municipios(municipios_mostrar):
    # Cargar datos del CSV
    print(municipios_mostrar)
    print("muniiii-----------")
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

    # Agregar la línea que une los marcadores
    ruta_coords = []
    for municipio in municipios_mostrar:
        coords = municipios_filtrados[municipios_filtrados['NOM_MUN'] == municipio][['LAT_DEC', 'LON_DEC']].values.tolist()[0]
        ruta_coords.append(coords)
    folium.PolyLine(locations=ruta_coords, color='blue', weight=3).add_to(mexico_map)

    # Mostrar mapa
    mexico_map.save("route.html")

# Llamar a la función para ejecutar el código
municipios_mostrar = ['Aguascalientes', 'Durango', 'Zacatecas']
mostrar_ruta_municipios(municipios_mostrar)
