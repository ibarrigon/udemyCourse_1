# Work with docker

## Start container
docker-compose up -d

## Stop container
docker-compose stop

## image name
udemycourse_1-app-1

## Go inside image

docker exec -it udemycourse_1-app-1 bash

## Run python interpreter
stable version. If docker image is upgraded, need to change 3.12 for the new version
python3.12

## Run file
python3.12 <file.py>

## Install third party modules or libraries
pip install <name>

# Proyects in daily_proyects

## Link
https://dailypythonprojects.substack.com/

## Solutions
Every day i recived an exercise. In file with format `ex<date(yyyymmdd)>.py` it's a comment with the problem and the 
codified solution

# librerias

pandas: open files (csv, json, excel, ...)

Notebooks:
ipython: better printing for large text
Jupyter: (Notebook) third-party library. To use online https://colab.research.google.com/#create=true

Open excel
openpyxl
xlrd: old excel files

Coordinates:
geopy

Images:
opencv-python