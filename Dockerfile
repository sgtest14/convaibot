FROM rasa/rasa:3.1.0-full
USER root
WORKDIR /app
COPY . /app
COPY ./data /app/data
RUN rasa train -c ./config.yml -d ./domain.yml --data ./data --debug
VOLUME /app
VOLUME /app/data
VOLUME /app/models
CMD ["run", "--cors" ,"*", "-m" ,"/app/models" ,"--enable-api","--endpoints" ,"endpoints.yml" ,"--debug"]