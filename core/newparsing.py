import numpy as np


bilingual_key = "........................."

def find_bilingual(document: str):
    return document.find(bilingual_key)

def check_number(paragragh: str):
    paragragh = "".join(paragragh.split())
    if paragragh.isnumeric():
        return True
    return False

def parsing_meta(document: str):
    document = " " + document
    for i in range(len(document)):
        if document[i] == "[":
           for j in range(i, len(document)):
               if document[j] == "]":
                   if check_number(document[i+1:j]):
                       return i
    return -1

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

def parsing_body(document: str):
    
    check_paragraph_exit = np.zeros(10005)
    check_paragraph_exit = check_paragraph_exit.tolist()
    paragraghs = document.split("[")
    paragraghs_parsing = []
    current_paragraph = 0

    for i in range(len(paragraghs)):
        paragragh = paragraghs[i]
        if paragragh.find("]") == -1: continue

        key = paragragh[:paragragh.find("]")]
        if not check_number(key): continue
        if not check_paragraph(key, check_paragraph_exit): continue
        check_paragraph_exit[int(key)] = 1
        concat_paragraph = " ".join(paragraghs[current_paragraph:i+1])
        current_paragraph = i + 1
        paragraghs_parsing.append(concat_paragraph)
    return paragraghs_parsing

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

    return meta, bodytop, bodybot

with open("D:\Lab\Coliee_2023_task12\data\\000127.txt", 'r') as myfile:
    data = myfile.read()
# x = parsing_body(data)
# for i in x:
#     print(i)
# print(parsing_document(data)[0])
print(parsing_document(data)[2])