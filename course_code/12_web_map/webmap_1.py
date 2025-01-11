import folium

# base Map
map = folium.Map(location = [80, -100], zoom_start = 6) 
# coordinates for north alaska. You can put any other values. [-90:90, -128:128]

map.save('./course_code/12_web_map/maps/generated_map_1.html')