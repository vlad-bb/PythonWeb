FROM python:3.10

WORKDIR /docker

EXPOSE 8001

COPY . /docker

RUN pip install -r requirements.txt

CMD [ "python", "main.py" ]