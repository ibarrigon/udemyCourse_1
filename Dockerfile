FROM python:3.12-bookworm

RUN useradd --create-home --shell /bin/bash app_user

WORKDIR /home/app_user/data

RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get -y install build-essential

# required almost for opencv-python
RUN apt-get -y install libopencv-*

RUN pip install --upgrade pip setuptools wheel

# work with files: csv, json, excel, ...
RUN pip install pandas

# Excel files
RUN pip install openpyxl xlrd

# coordinates
RUN pip install geopy

# install OpenCV for process images
RUN pip install opencv-python

# python notebooks
# RUN pip install ipython jupyter

USER app_user

CMD ["bash"]