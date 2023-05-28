FROM alpine

RUN apk add --no-cache python3-dev
RUN apk add --update py3-pip 
RUN apk add curl
RUN apk add --no-cache bash

WORKDIR /app

COPY requirements.txt /app
RUN pip3 install -r requirements.txt

COPY app.py /app
COPY db.py /app
COPY templates/ /app/templates

EXPOSE 5000

CMD ["flask", "run", "--host", "0.0.0.0"]

