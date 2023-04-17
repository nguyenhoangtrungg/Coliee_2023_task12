import numpy as np

from langdetect import detect

import getyear
import newparsing


suppressed_list = ["FRAGMENT_SUPPRESSED", "REFERENCE_SUPPRESSED", "CITATION_SUPPRESSED", "DATE_SUPPRESSED"]

suppressed = "_SUPPRESSED"

catch_list1 = ["Background", "BACKGROUND", "background", " II", " I", "II.", "I.", "1.", "2.", "ii", "ii.", "i.", "Fact", "FACT", "fact"]
catch_list2 = ["Issue", "ISSUE", "issue", " III", "III.", "3.", "IV", "iii", "iii."]

def find_suppressed(paragragh: str):
    paragragh = paragragh.lower()
    local_suppressed = suppressed.lower()
    flag = paragragh.find(local_suppressed)
    if flag != -1: return True
    return False

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
    suppressed_parapraghs = []
    for i in range(len(parapraghs)):
        parapraghs[i] = clean_content(parapraghs[i])
        if suppressed_flag:
            if find_suppressed(parapraghs[i]):
                suppressed_parapraghs.append(parapraghs[i])
                suppressed_parapraghs[-1] = clean_suppressed(suppressed_parapraghs[-1])

    if suppressed_flag: return suppressed_parapraghs
    return parapraghs

def get_number_of_paragraph(paragraghs: str):
    paragraghs = paragraghs.split(' ')
    return len(paragraghs)

def detect_language(paragraghs: list, threshold: int):
    paragragh = ""
    for para in paragraghs:
        if get_number_of_paragraph(paragragh) > threshold: break
        paragragh += para
    try:
        language = detect(paragragh)
    except:
        return False
    if language == "en": 
        return True
    return False

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

def choose_body(bodytop: list, bodybot: list, threshold: int):
    lan_top = detect_language(bodytop, threshold)
    lan_bot = detect_language(bodybot, threshold)
    if lan_top:
        body = newparsing.parsing_body(bodytop)
    elif lan_bot:
        body = newparsing.parsing_body(bodybot)
    else: 
        return ""
    return body

def run_preprocessing(document: str, suppressed_flag: bool):
    parsing_doc = newparsing.parsing_document(document)
    meta = parsing_doc["meta"]
    bodytop = parsing_doc["bodytop"]
    bodybot = parsing_doc["bodybot"]
    year = getyear.get_year(document)
    
    body = choose_body(bodytop, bodybot, 1000)

    if suppressed_flag:
        meta = clean_suppressed(clean_content(meta))
        body = clean_document(body, suppressed_flag)
    else:
        meta = clean_content(meta)
        body = clean_document(body, suppressed_flag)
    body_year = getyear.concat_list_year(body, year)

    return {
        "meta": meta,
        "body": body_year,
    }

