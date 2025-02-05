FROM python:3.12-bookworm

WORKDIR /app

# required almost for opencv-python
RUN apt-get -y install libopencv-*
RUN apt-get -y install libgl1-mesa-glx libglib2.0-0

RUN pip3 install --upgrade pip setuptools wheel
RUN pip3 install pandas
RUN pip3 install openpyxl
RUN pip3 install xlrd
RUN pip3 install geopy
RUN pip3 install opencv-python
RUN pip3 install folium
RUN pip3 install bokeh

RUN pip3 install jupyter

EXPOSE 8888

ENV NAME World

CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]