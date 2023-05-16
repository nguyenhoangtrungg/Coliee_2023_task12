import numpy as np


bilingual_key = "........................."

"""
find the location of bilingual in document

@param document: document to find bilingual
@return location of bilingual, -1 if not found
"""
def find_bilingual(document: str):
    return document.find(bilingual_key)

"""
check paragragh is number or not

@param paragragh: paragragh to check
@return True if paragragh is number, False if not
"""
def check_number(paragragh: str):
    paragragh = "".join(paragragh.split())
    if paragragh.isnumeric():
        return True
    return False

"""
Check if the sentences are in the correct order
check rule is have an id of sentences before and dont have id of sentences after

@param id: id of paragragh
@param check_paragraph_exit: list of paragragh is exist
"""
def check_paragraph(id: str, check_paragraph_exit):
    id = int(id)
    id_min = max(0, id - 6)
    id_max = min(10005, id + 6)

    for i in range(id, id_max):
        if check_paragraph_exit[i] == 1:
            return False

    if id < 6: 
        return True

    for i in range(id, id_min, -1):
        if check_paragraph_exit[i] == 1:
            return True
    return False

"""
find the location of meta in document
using rule: meta is in the first of document and before 
a sencentes have format [number]

@param document: document to find meta
@return location of meta, -1 if not found
"""
def parsing_meta(document: str):
    document = " " + document
    for i in range(len(document)):
        if document[i] == "[":
           for j in range(i, len(document)):
               if document[j] == "]":
                   local_num = document[i+1:j]
                   if check_number(local_num) and int(local_num) < 3:
                       return i
    return -1

"""
parse paragragh in document
using rule: paragragh is in the format fisrt word [number]

@paragragh document: document to parse
@return list of paragragh
"""
def parsing_body(document: str):
    
    check_paragraph_exit = np.zeros(10005)
    check_paragraph_exit = check_paragraph_exit.tolist()
    paragraghs = document.split("[")
    paragraghs_parsing = []

    for i in range(len(paragraghs)):
        paragragh = paragraghs[i]
        if paragragh.find("]") == -1: continue

        key = paragragh[:paragragh.find("]")]
        if not check_number(key): 
            paragraghs_parsing[-1] += "[" + paragragh
            continue
        if not check_paragraph(key, check_paragraph_exit):
            paragraghs_parsing[-1] += "[" + paragragh
            continue
        check_paragraph_exit[int(key)] = 1
        paragraghs_parsing.append("[" + paragragh)
    return paragraghs_parsing

"""
parse document to meta, bodytop, bodybot
using rule: meta is in the first of document
if have bilingual, bodytop is before bilingual, bodybot is after bilingual

@param document: document to parse
@return dictionary of meta, bodytop, bodybot
"""
def parsing_document(document: str):
    location_meta = parsing_meta(document) - 1
    if location_meta < 0: location_meta = 0
    meta = document[:location_meta]
    body = document[location_meta:]

    bilingual = find_bilingual(body)
    if bilingual != -1:
        bodytop = body[:bilingual]
        bodybot = body[bilingual:]
    else:
        bodytop = body
        bodybot = ""

    if bodybot != "":
        location_metabot = parsing_meta(bodybot) - 1
        if location_metabot < 0: location_metabot = 0
        bodybot = bodybot[location_metabot:]

    return {
        "meta": meta,
        "bodytop": bodytop,
        "bodybot": bodybot
    }

# with open("D:\Lab\Coliee_2023_task12\data\\000127.txt", 'r') as myfile:
#     data = myfile.read()
# x = parsing_body(data)
# for i in x:
#     print(i)
# print(parsing_document(data)[0])
# print(parsing_document(data)[2])