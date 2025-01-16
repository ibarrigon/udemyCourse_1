FROM python:3.12-bookworm

RUN useradd --create-home --shell /bin/bash app_user

WORKDIR /home/app_user/data

RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get -y install build-essential

# required almost for opencv-python
RUN apt-get -y install libopencv-*
RUN apt-get -y install libgl1-mesa-glx libglib2.0-0

RUN pip3 install --upgrade pip setuptools wheel

# work with files: csv, json, excel, ...
RUN pip3 install pandas

# Excel files
RUN pip3 install openpyxl xlrd

# coordinates
RUN pip3 install geopy

# install OpenCV for process images
RUN pip3 install opencv-python 
# Maybe you required: RUN pip3 install opencv-python-headless 

# python notebooks
# RUN pip install ipython jupyter

RUN pip3 install folium
# RUN pip3 install jinja2 # included inside folium

USER app_user

CMD ["bash"]