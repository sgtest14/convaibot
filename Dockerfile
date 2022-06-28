FROM rasa/rasa:3.1.0-full
USER root
WORKDIR /app
COPY . /app
COPY ./data /app/data

RUN pip3 install boto3
ARG AWS_DEFAULT_REGION="us-east-1"
ARG AWS_SECRET_ACCESS_KEY="5EqoCvAFT48OuZ0XuHQu+zQ48pac2FqKAzBERHMs"
ARG AWS_ACCESS_KEY_ID="AKIA4NB3NEIHHJ64F62B"
ARG BUCKET_NAME="convai"
ARG AWS_ENDPOINT_URL="https://s3.us-east-1.amazonaws.com"

ENV AWS_DEFAULT_REGION=${AWS_DEFAULT_REGION}
ENV AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY}
ENV AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID}
ENV BUCKET_NAME=${BUCKET_NAME}
ENV AWS_ENDPOINT_URL=${AWS_ENDPOINT_URL} 

RUN rasa run -m models.tar.gz --enable-api --log-file out.log --remote-storage aws
VOLUME /app
VOLUME /app/data
VOLUME /app/models
CMD ["run", "--cors" ,"*", "-m" ,"/app/models" ,"--enable-api","--endpoints" ,"endpoints.yml" ,"--debug"]