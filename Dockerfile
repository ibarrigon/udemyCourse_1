FROM python:3.12-bookworm

RUN useradd --create-home --shell /bin/bash app_user

WORKDIR /home/app_user/data

RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get -y install build-essential

RUN pip install --upgrade pip setuptools wheel
RUN pip install pandas

USER app_user

CMD ["bash"]