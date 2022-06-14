from opensearchpy import OpenSearch
import sys

import opensearchpy
host, port = "127.0.0.1", 9200
client = OpenSearch(hosts = [{"host" : host, "port" : port}])
index_name = "sample"
document = {
  'title': 'Moneyball',
  'director': 'Bennett Miller',
  'year': '2011'
}
id = '1'
response = client.index(
    index = index_name,
    body = document,
    id = id,
    refresh = True
)
print(response)