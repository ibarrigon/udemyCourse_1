# Address to coordinates
# We are going to use Nominatim() in the next video. Nominatim() currently has a bug. To fix this problem, whenever you see these lines in the next video:
# from geopy.geocoders import Nominatim
# nom = Nominatim()
# change them to these
# 
# from geopy.geocoders import ArcGIS
# nom = ArcGIS()
# The rest of the code remains the same.
# 1056 Sanchez St,San Francisco,California,USA
#
# from geopy.geocoders import Nominatim
#
# nom = Nominatim()
# nom.geocode('1056 Sanchez St, San Francisco, California, USA')

from geopy.geocoders import ArcGIS
import pandas

nom = ArcGIS()
location = nom.geocode('1056 Sanchez St, San Francisco, California, USA')
# Location(1056 Sanchez St, San Francisco, California, 94114, (37.752156484757, -122.429962205901, 0.0))
# if cant find None is returned
print(location.latitude)
print(location.longitude)

data_csv = pandas.read_csv('files/supermarkets.csv')
data_csv['Address'] = data_csv['Address'] + ', ' + data_csv['City'] + ', ' + data_csv['State'] + ', ' + data_csv['Country']
data_csv['Coordinates'] = data_csv['Address'].apply(nom.geocode)
data_csv['Latitude'] = data_csv['Coordinates'].apply(lambda x: x.latitude if x != None else None)
data_csv['Longitude'] = data_csv['Coordinates'].apply(lambda x: x.longitude if x != None else None)