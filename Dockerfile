FROM python:3.7-slim


# set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set working directory
WORKDIR /usr/src/app
RUN mkdir tmp

# ---- Python Packages ----#
COPY requirements.txt  /usr/src/app/requirements.txt
RUN pip install -r requirements.txt


COPY app_downsizing.py /usr/src/app/app_downsizing.py

EXPOSE 80

#CMD bash
CMD ["python", "app_downsizing.py"]