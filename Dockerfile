FROM rasa/rasa:3.1.0-full
USER root
WORKDIR /app
COPY . /app
COPY ./data /app/data
VOLUME /app
VOLUME /app/data
CMD ["run", "--cors" ,"*", "--enable-api","--endpoints" ,"endpoints.yml" ,"--debug"]