from elasticsearch import Elasticsearch
es = Elasticsearch(['http://localhost:49154']) # connecting to elasticsearch
es.ping()