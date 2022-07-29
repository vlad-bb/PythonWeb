# pull official base image
FROM python:3.10

# set work directory
WORKDIR /src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /src/app/requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY . /src/app/

#EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5440", "wsgi:app"]