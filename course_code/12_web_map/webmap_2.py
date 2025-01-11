import folium

# Add points
# Madrid Coordinates. In course thay use Stamen Terrain, but actualy it isn't free
map = folium.Map(location = [40.41751246336078, -3.704411462653831], zoom_start = 6, tiles = 'OpenTopoMap')
map.add_child(folium.Marker(location = [40.40, -3.704411462653831], popup = 'Hi. I am a Marker', icon = folium.Icon(color = 'green')))

map.save('./course_code/12_web_map/maps/generated_map_2.html')