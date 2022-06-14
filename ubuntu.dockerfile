FROM ubuntu

RUN mkdir -p /app
WORKDIR /app
COPY mw_server.py /app/

RUN apt-get update
RUN apt-get install -y vim
RUN apt-get install -y curl
RUN apt-get install -y iputils-ping
RUN apt-get install -y python3
RUN apt-get install -y pip

RUN pip3 install gandan
RUN pip3 install opensearch-py
RUN pip3 install pandas

EXPOSE 8080

CMD ["bash"]
