FROM ubuntu

RUN mkdir -p /apigw
WORKDIR /apigw
COPY apigw/request_naver.py /apigw/
COPY apigw/request_daum.py /apigw/
COPY apigw/apigw.py /apigw/

RUN apt-get update
RUN apt-get install -y curl
RUN apt-get install -y iputils-ping
RUN apt-get install -y python3
RUN apt-get install -y pip

RUN pip3 install requests
RUN pip3 install flask
RUN pip3 install flask_restx
RUN pip3 install bs4

EXPOSE 3000

ENV PYTHONPATH /apigw:$PYTHONPATH

CMD ["python3", "/apigw/apigw.py"]
