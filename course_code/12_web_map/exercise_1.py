# Coding Exercise
#
# Replace the icon markers we added in the previous lectures with circle markers
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

map = folium.Map(location = [40.41751246336078, -3.704411462653831], zoom_start = 6, tiles = 'OpenTopoMap')
fg = folium.FeatureGroup(name = 'Volcanoes')

for lt, ln, name, elevation in zip(lat, lon, names, elevations):
    fg.add_child(
        folium.CircleMarker(
            location = [lt, ln], 
            radius = 6, # six pixels radius
            popup = folium.Popup(folium.IFrame(html=html % (name, name, elevation), width=200, height=100)), 
            fill_color = color_by_elevation(elevation),
            color = color_by_elevation(elevation),
            fill_opacity = 0.7
        )
    )

map.add_child(fg)

map.save('./course_code/12_web_map/maps/exercise_1.html')
