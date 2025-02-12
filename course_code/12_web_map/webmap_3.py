import folium

# plain add coordinates
map = folium.Map(location = [40.41751246336078, -3.704411462653831], zoom_start = 6, tiles = 'OpenTopoMap')
feature_group = folium.FeatureGroup(name = 'My map')
feature_group.add_child(folium.Marker(location = [40.40, -3.704411462653831], popup = 'Hi I am a Marker', icon = folium.Icon(color = 'green')))
feature_group.add_child(folium.Marker(location = [40.30, -3.704411462653831], popup = 'Hi I am a Marker', icon = folium.Icon(color = 'green')))
feature_group.add_child(folium.Marker(location = [40.20, -3.704411462653831], popup = 'Hi I am a Marker', icon = folium.Icon(color = 'green')))
 
map.add_child(feature_group)

map.save('./course_code/12_web_map/maps/generated_map_3.html')
