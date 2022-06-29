FROM rasa/rasa:3.1.0-full
USER root
WORKDIR /app
COPY . /app
COPY ./data /app/data
COPY ./models /app/models

VOLUME /app
VOLUME /app/data
VOLUME /app/models
CMD ["run", "--cors" ,"*", "-m" ,"models" ,"--enable-api","--endpoints" ,"endpoints.yml" ,"--debug"]