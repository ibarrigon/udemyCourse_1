FROM python:3.14.0a1-slim

RUN useradd --create-home --shell /bin/bash app_user

WORKDIR /home/app_user/data

RUN pip install --upgrade pip
RUN pip install pandas

USER app_user

CMD ["bash"]