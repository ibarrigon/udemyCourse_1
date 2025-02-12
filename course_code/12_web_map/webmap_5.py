import pandas
import folium

volcanoes = pandas.read_csv('./course_code/12_web_map/files/Volcanoes.csv')

map = folium.Map(location = [40.41751246336078, -3.704411462653831], zoom_start = 6, tiles = 'OpenTopoMap')
feature_group = folium.FeatureGroup(name = 'Volcanoes')

lat = list(volcanoes['LAT'])
lon = list(volcanoes['LON'])
elevations = list(volcanoes['ELEV'])
names = list(volcanoes['NAME'])

for lt, ln, name, elevation in zip(lat, lon, names, elevations):
    feature_group.add_child(folium.Marker(location = [lt, ln], popup = name + f'({elevation} m)', icon = folium.Icon(color = 'green')))

map.add_child(feature_group)

map.save(f'./course_code/12_web_map/maps/generated_map_5.html')
