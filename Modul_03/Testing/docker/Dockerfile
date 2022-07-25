FROM python:3

WORKDIR /app

COPY . ./

EXPOSE 8001

RUN pip install --upgrade pip

COPY . .

CMD [ "python", "./app.py" ]