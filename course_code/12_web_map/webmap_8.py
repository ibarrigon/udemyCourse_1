import pandas
import folium

map = folium.Map(location = [40.41751246336078, -3.704411462653831], zoom_start = 6, tiles = 'OpenTopoMap')
feature_group = folium.FeatureGroup(name = 'Info in map')
feature_group.add_child(folium.GeoJson(data = (open('./course_code/12_web_map/files/world.json', 'r', encoding = 'utf-8-sig').read())))
map.add_child(feature_group)

map.save('./course_code/12_web_map/maps/generated_map_8.html')
