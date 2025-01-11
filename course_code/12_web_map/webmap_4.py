import folium

# Using a loop to add coordinates
map = folium.Map(location = [40.41751246336078, -3.704411462653831], zoom_start = 6, tiles = 'OpenTopoMap')
fg = folium.FeatureGroup(name = 'My map')
for coordinates in [[40.40, -3.70], [40.30, -3.60], [40.20, -3.5]]:
    fg.add_child(folium.Marker(location = coordinates, popup = 'Hi I am a Marker', icon = folium.Icon(color = 'green')))

map.add_child(fg)

map.save('./course_code/12_web_map/maps/generated_map_4.html')

