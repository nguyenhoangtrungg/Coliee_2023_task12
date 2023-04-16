import numpy as np

from langdetect import detect

import getyear
import parsing


suppressed_list = ["FRAGMENT_SUPPRESSED", "REFERENCE_SUPPRESSED", "CITATION_SUPPRESSED", "DATE_SUPPRESSED"]

suppressed = "_SUPPRESSED"

catch_list1 = ["Background", "BACKGROUND", "background", " II", " I", "II.", "I.", "1.", "2.", "ii", "ii.", "i.", "Fact", "FACT", "fact"]
catch_list2 = ["Issue", "ISSUE", "issue", " III", "III.", "3.", "IV", "iii", "iii."]

def clean_suppressed(paragragh: str):
    for suppressed in suppressed_list:
        paragragh = paragragh.replace(suppressed, "")
    return paragragh

def clean_content(paragragh: str):
    paragragh = paragragh.replace("\n", " ")
    paragragh = paragragh.replace("<", "").replace(">", "").replace("[]", "").replace("[ ]", "")
    paragragh = paragragh.replace('?','.')
    paragragh = paragragh.replace('!','.')
    paragragh = paragragh.replace('。','.')
    paragragh = " ".join(paragragh.split())
    return paragragh

def clean_document(parapraghs: list, suppressed_flag: bool):
    for i in range(len(parapraghs)):
        parapraghs[i] = clean_content(parapraghs[i])
        if suppressed_flag:
            parapraghs[i] = clean_suppressed(parapraghs[i])

    return parapraghs

def remove_index_paragraph(paragragh: str):
    
    paragragh = paragragh.replace('?','.')
    paragragh = paragragh.replace('!','.')
    paragragh = paragragh.replace('。','.')

    paragragh = paragragh.split('.')

    index = []

    while len(paragragh[-1].split(' ')) <= 5:
        index.append(paragragh[-1])
        if len(paragragh) == 1: 
            return '.'.join(paragragh)
        paragragh.pop()
    
    while len(paragragh[-1].split(' ')) <= 3:
        index.append(paragragh[-1])
        if len(paragragh) == 1: 
            return '.'.join(paragragh)
        paragragh.pop()

    return '.'.join(paragragh)

def del_dup(paragraghs: list): 

    for j in range(len(paragraghs)):
        _here = paragraghs[j]
        for k in range(len(_here)):
            lolo = 0
            if _here[k] == "]":
                lolo = k + 1
                break
        find_dup = _here[:lolo]
        duplo = _here.find(find_dup, 1)
        if duplo != -1:
            paragraghs[j] = _here[:duplo]
    return paragraghs

def get_body(_link):
    dou = 0
    f = open(_link)
    document = f.read()
    document = "\n" + document.replace("\n ", "\n").replace(" \n", "\n")
    document_year = getyear.getYear(document)

    raw = parsing.findList(document, 0)
    meta = raw[-2]

    if(raw[1] < 0):
        print(_link)

    if len(raw[0]) > (raw[1] + 5):
        dou = 1
        lenlen = raw[4]
        body = raw[0][:lenlen+1]

        if detect(body[0]) != "en":
            body = raw[0][lenlen+1:]
            dou = 2
        else:
            body[-1] = body[-1].split(".........................")[0]
            # ....................
            # .........................

    else: body = raw[0]
    body = clean_document(body)
    
    clear_body = del_dup(body)
    oul = []
    for i in range(len(clear_body)):
        hihihi = remove_index_paragraph(clear_body[i])
        clear_body[i] = hihihi[0]
        oul.append(hihihi[1])

    return meta, clear_body, dou, document_year, oul