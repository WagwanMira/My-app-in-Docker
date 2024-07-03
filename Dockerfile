FROM python:3.8.10

WORKDIR /myapp

COPY . /myapp

#ADD docker-entrypoint.sh /docker-entrypoint.sh

RUN pip install -r requirements.txt 

#RUN chmod +x  /docker-entrypoint.sh



CMD ["python", "server.py"]

#ENTRYPOINT /docker-entrypoint.sh 
