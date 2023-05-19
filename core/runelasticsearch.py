from elasticsearch import Elasticsearch
import json
import os
import argparse

"""
login to elasticsearch server with password
"""
def login(account, password):
    client = Elasticsearch(hosts="https://localhost:9200", basic_auth=(account, password), verify_certs=False)
    return client

"""
mapping index to elasticsearch server using nested type 

@param client: client to connect to elasticsearch server
@param _index: index name
"""
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

"""
indexing data to elasticsearch server using nested type, 
in index have id of document, num is order in document, 
paragraph is raw data, year is year in document

@param client: client to connect to elasticsearch server
@param _index: index name
@param input_list: list of data to index
"""
def indexing(client, _index, input_list):

    for i in range(len(input_list)):
        _id = input_list[i]["id"]
        _label = input_list[i]["label"]
        _paragraphs = input_list[i]["body"]
        ls_paragraphs = []

        for i_p in range(len(_paragraphs)):
            para_doc = {
                "id": _id,
                "num": i_p,
                "paragraph": _paragraphs[i_p]["paragraph"],
                "year": _paragraphs[i_p]["year"],
            }
            ls_paragraphs.append(para_doc)

        _indexing = {
            "id": _id,
            "label": _label,
            "paragraphs": ls_paragraphs
        }
        response_indexing = client.index(index=_index, body=_indexing)

"""
searching data in elasticsearch server using nested type.
for each sentence in the query search all the sentences related 
to it provided that the year of the search sentence is greater 
than the year of the searched sentence.


@param client: client to connect to elasticsearch server 
@param _index: index name
@param _query: query to search
@param qr_year: year of query
@param lenout: number of result
@return result of searching have 200*lenout results  sorted by score
"""
def searching(client, _index, _query: str, qr_year, lenout):
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

"""
get result of searching have format in4 is id of document,
num is order in document, paragraph is raw data, 
score is score of result in BM25. Take 200 results with
the highest score mean the best sentence with the sentence queried

@param res: result of searching
@param id_check: id of query
@return result of searching have 200 results sorted by score
"""
def get_query(res, id_check):

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

"""
take result into format to write to json file
with each sencentes have 200 results with the highest score

@param _data: data to get result
@return result of searching
"""
def get_data(_data): 
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
        
        out_query = get_query(res, _data["id"])
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

"""
write result to json file

@param input_list: list of data
@param link_folder_out: link to output folder
"""
def write_data(input_list, link_folder_out):
    
    for id in range(len(input_list)):
        data_doc = get_data(input_list[id])

        result = json.dumps(data_doc, indent=2, ensure_ascii=False)
        output_link = link_folder_out + "\\" + str(input_list[id]["id"]).split(".")[0] + ".json"
        myjsonfile = open(output_link, "w", encoding="utf-8")
        myjsonfile.write(result)
        myjsonfile.close()


"""
concat input file to list

@param input_link: link to input file
@return list of data
"""
def concat_file(input_link):
    output = []
    link = os.listdir(input_link)
    for local in link:
        with open(input_link + "\\" + local, "r", encoding="utf-8") as f:
            _data = json.load(f)
        output.append(_data)

    return output

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Elasticsearch.')

    parser.add_argument("-acc", "--account", help="Account of Elasticsearch.", default="elastic", type=str)
    parser.add_argument("-pw", "--password", help="Password of Elasticsearch.", default="123456", type=str)
    parser.add_argument("-ix", "--index", help="Index name.", default="es_coliee", type=str)

    parser.add_argument("-mo", "--mode", help="Set mode", default="111", type=str)

    parser.add_argument("-il", "--input_link", help="link of input", default="\data\output", type=str)
    parser.add_argument("-ol", "--output_link", help="link of folder output.", default="\data\es_output", type=str)

    args = parser.parse_args()

    account = args.account
    password = args.password
    _index = args.index

    input_link = args.input_link
    output_link = args.output_link
    mode = args.mode
    input_list = concat_file(input_link)
    client = login(account, password)
    if mode[0] == "1":
        mapping(client, _index)
    if mode[1] == "1":
        indexing(client, _index, input_list)
    if mode[2] == "1":
        write_data(input_list, output_link)
