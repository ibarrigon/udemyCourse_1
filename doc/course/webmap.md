# Wbe Map

## description

The files stored in folder 12_web_map build a program that generates interactive web maps with Python. The program 
combines the core Python building blocks such as conditionals, for-loops, functions, and file processing with 
the extras of a third-party Python library used to generate beautiful web maps. 

## Required libraries

1. folium
2. jinja2 (included)
4. pandas

## Tiles to use

The tiles used on course can't be used. There's a list (11/01/2025). Choose what you like.
+ OpenTopoMap
+ cartodbpositron
+ [More info](https://python-visualization.github.io/folium/latest/getting_started.html#Choosing-a-tileset)

## Add poligons

In file webmap_8.py we have a file .json with all the coordinates of the countries. Passing it to folium it can 
represent and paint it.

## Addo colors

In file webmap_9.py we have the work from previous lesson and add colors representing the population

## Control layers

In file webmap_10.py we added a control box to deactivate layers. At the end, we divided the info in two backgrounds 
to activate or deactivate it separately


## Alternative

This code is to generate a file name based in the time

from time import gmtime, strftime
filetime = strftime("%Y%m%d%H%M%S", gmtime())
map.save(f'./course_code/12_web_map/maps/generated_map_{filetime}.html')