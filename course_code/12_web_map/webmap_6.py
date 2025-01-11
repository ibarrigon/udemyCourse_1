import pandas
import folium

volcanoes = pandas.read_csv('./course_code/12_web_map/files/Volcanoes.csv')
lat = list(volcanoes['LAT'])
lon = list(volcanoes['LON'])
elevations = list(volcanoes['ELEV'])
names = list(volcanoes['NAME'])

html = """
Volcano: <br/>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br />
Height: %s m
"""

map = folium.Map(location = [40.41751246336078, -3.704411462653831], zoom_start = 6, tiles = 'OpenTopoMap')
fg = folium.FeatureGroup(name = 'Volcanoes')

for lt, ln, name, elevation in zip(lat, lon, names, elevations):
    iframe = folium.IFrame(html=html % (name, name, elevation), width=200, height=100)
    fg.add_child(folium.Marker(location = [lt, ln], popup = folium.Popup(iframe), icon = folium.Icon(color = 'green')))

map.add_child(fg)

map.save('./course_code/12_web_map/maps/generated_map_6.html')
