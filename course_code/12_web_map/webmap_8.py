import pandas
import folium

map = folium.Map(location = [40.41751246336078, -3.704411462653831], zoom_start = 6, tiles = 'OpenTopoMap')
fg = folium.FeatureGroup(name = 'Info in map')
fg.add_child(folium.GeoJson(data = (open('./course_code/12_web_map/files/world.json', 'r', encoding = 'utf-8-sig').read())))
map.add_child(fg)

map.save('./course_code/12_web_map/maps/generated_map_8.html')
