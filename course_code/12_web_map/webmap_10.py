import pandas
import folium

def color_by_elevation(elevation):
    if elevation < 1000:
        return 'green'
    
    if 1000 <= elevation < 3000: # This is between 1000 and 3000
        return 'orange'
    
    return 'red'

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

map = folium.Map(location = [40.41751246336078, -3.704411462653831], zoom_start = 6, tiles = 'cartodbpositron')
feature_group = folium.FeatureGroup(name = 'Volcanoes')

for lt, ln, name, elevation in zip(lat, lon, names, elevations):
    feature_group.add_child(
        folium.CircleMarker(
            location = [lt, ln], 
            radius = 6, # six pixels radius
            popup = folium.Popup(folium.IFrame(html=html % (name, name, elevation), width=200, height=100)), 
            fill_color = color_by_elevation(elevation),
            color = color_by_elevation(elevation),
            fill_opacity = 0.7
        )
    )

feature_group2 = folium.FeatureGroup(name = 'Population')
feature_group2.add_child(
    folium.GeoJson(
        data = (open('./course_code/12_web_map/files/world.json', 'r', encoding = 'utf-8-sig').read()),
        style_function = lambda item: {
            'fillColor': 'green' if item['properties']['POP2005'] < 10000000 
            else 'orange' if 10000000 <= item['properties']['POP2005'] < 20000000 else 'red'
        }
    )
)

map.add_child(feature_group)
map.add_child(feature_group2)
map.add_child(folium.LayerControl())

map.save('./course_code/12_web_map/maps/generated_map_10.html')
