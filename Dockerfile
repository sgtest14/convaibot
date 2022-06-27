WORKDIR /app

RUN pip install rasa==2.8.1

ADD config.yml config.yml
ADD domain.yml domain.yml
ADD endpoints.yml endpoints.yml
ADD credentials.yml credentials.yml