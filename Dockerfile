FROM rasa/rasa:3.1.0-full
USER root
WORKDIR /app
COPY . /app
COPY ./data /app/data
COPY ./models /app/models

ADD credentials.yml credentials.yml 
ADD endpoints.yml endpoints.yml
ADD config.yml config.yml
ADD domain.yml domain.yml

VOLUME /app
VOLUME /app/data
VOLUME /app/models