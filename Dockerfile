USER root
WORKDIR /app
COPY . /app
COPY ./data /app/data
COPY ./models /app/models

VOLUME /app
VOLUME /app/data
VOLUME /app/models