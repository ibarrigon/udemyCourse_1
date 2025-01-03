FROM python:3.14.0a1-slim

RUN useradd --create-home --shell /bin/bash app_user

WORKDIR /home/app_user/data

# COPY requirements.txt ./

# RUN pip install --no-cache-dir -r requirements.txt

USER app_user

CMD ["bash"]