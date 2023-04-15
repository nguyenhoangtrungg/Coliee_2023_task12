from elasticsearch import Elasticsearch
import os
import json

# login to elasticsearch with key
def login():
    client = Elasticsearch(hosts="https://localhost:9200", basic_auth=("elastic", ELASTIC_PASSWORD), verify_certs=False)
    return client

# mapping 
# _index: index name
def mapping(client, _index):
    _mapping = {
        "mappings": {
            "properties": {
                "paragraphs": {
                "type": "nested",
                    "properties": {
                        "paragraph": {
                        "type": "text"
                        }
                    }
                }
            }
        }
    }

    response = client.indices.create(
        index = _index,
        body = _mapping,
        ignore = 400
    )

# indexing
# _index: index name
# input_link: link to input file
def indexing(client, _index, input_link):

    with open(input_link, "r", encoding="utf-8") as f:
        _data = json.load(f)

    for i in range(len(_data)):
        _id = _data[i]["id"]
        _label = _data[i]["label"]
        _paragraphs = _data[i]["body"]
        ls_paragraphs = []

        for i_p in range(len(_paragraphs)):
            para_doc = {
                "id": _id,
                "num": i_p,
                "paragraph": _paragraphs[i_p]["raw"],
                "year": _paragraphs[i_p]["year"],
            }
            ls_paragraphs.append(para_doc)

        _indexing = {
            "id": _id,
            "label": _label,
            "paragraphs": ls_paragraphs
        }
        response_indexing = client.index(index=_index, body=_indexing)

# search
# _index: index name
# _query: query
# qr_year: query year
# lenout: number of output
def searching(client, _index, _query, qr_year, lenout):
    query = {
        "query": {
            "nested": {
                "path": "paragraphs",
                "score_mode": "max",
                "query": {
                        "bool": {
                            "must": [
                                { "match": { "paragraphs.paragraph": _query}},
                            ],
                            "filter": [
                                { "range": { "paragraphs.year": {"lte": qr_year}}},
                            ]
                        }
                    },
                "inner_hits": { 
                    "size": lenout,
                    "sort": [{"_score": "desc"}]
                    }
            }
        }
    }
    res = client.search(index=_index, body=query, size=201, sort = {"_score": {"order": "desc"}})
    return res

# get query: return top 200 results
# res: result of searching
# id_check: id of query
def getQuery(res, id_check):

    _out = []
    out_score = []

    for j in range(len(res["hits"]["hits"])):
        for k in range(len(res["hits"]["hits"][j]["inner_hits"]["paragraphs"]["hits"]["hits"])):
            _out.append(res["hits"]["hits"][j]["inner_hits"]["paragraphs"]["hits"]["hits"][k])

    for j in range(len(_out)):
        if _out[j]["_source"]["id"] == id_check: continue
        score_data = {
            'in4': _out[j]["_source"]["id"],
            'num': _out[j]["_source"]["num"],
            'paragraph': _out[j]["_source"]["paragraph"],
            'score': _out[j]["_score"],
        }
        out_score.append(score_data)

    out_score = sorted(out_score, key=lambda k: k['score'], reverse=True)

    out_score = out_score[:200]

    return out_score

# get data: get all data of query
# _data: data of query
def getData(_data): 
    _out_body = []
    for i in range(len(_data["body"])):
        _query = _data["body"][i]["paragraph"]
        qr_year = _data["body"][i]["year"]
        if qr_year == 0: qr_year = 2021

        try:
            lenout = 100
            res = searching(client, _index, _query, qr_year, lenout)
        except:
            continue
        
        out_query = getQuery(res, _data["id"])
        body_data = {
            'paragraph': _query,
            'top_score': out_query
        }
        
        _out_body.append(body_data)
    dataa = {
        'id': _data["id"],
        'label': _data["label"],
        'paragraphs_top_score': _out_body
    }
    return dataa

# write data to json file
def writeData(input_link, link_folder_out):
    with open(input_link, "r", encoding="utf-8") as f:
        _data = json.load(f)
    for id in range(len(_data)):
        data_doc = getData(_data[id])

        result = json.dumps(data_doc, indent=2, ensure_ascii=False)
        myjsonfile = open(link_folder_out + str(_data[id]["id"]) + ".json", "w", encoding="utf-8")
        myjsonfile.write(result)
        myjsonfile.close()
        
ELASTIC_PASSWORD = "TfO2an_x*5qCiwBcoAdE"
_index = "es_coliee_test"
input_link = "D:\Lab\Coliee\Code\Data\Output\\test_querylist.json"

link_folder_out = "D:\Lab\Coliee\demo\\"

client = login(_index)
# mapping(client, _index)
# indexing(client, _index, input_link)

writeData(input_link, link_folder_out)


