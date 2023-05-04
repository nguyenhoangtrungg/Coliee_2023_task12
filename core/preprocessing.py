from langdetect import detect

import getyear
import parsing
import getlabel


suppressed_list = ["FRAGMENT_SUPPRESSED", "REFERENCE_SUPPRESSED", "CITATION_SUPPRESSED", "DATE_SUPPRESSED"]

suppressed = "_SUPPRESSED"

catch_list1 = ["Background", "BACKGROUND", "background", " II", " I", "II.", "I.", "1.", "2.", "ii", "ii.", "i.", "Fact", "FACT", "fact"]
catch_list2 = ["Issue", "ISSUE", "issue", " III", "III.", "3.", "IV", "iii", "iii."]

"""
check if paragragh is header or not

@param paragragh: paragragh to check
@return True if paragragh have suppressed, False if not
"""
def find_suppressed(paragragh: str):
    paragragh = paragragh.lower()
    local_suppressed = suppressed.lower()
    flag = paragragh.find(local_suppressed)
    if flag != -1: return True
    return False

"""
clean index of paragragh
rule: clean sencentes have length <= 5 or <= 3

@param paragragh: paragragh to check
@return paragraph after clean
"""
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

"""
clean suppressed in paragragh

@param: paragragh to clean
@return paragragh after clean
"""
def clean_suppressed(paragragh: str):
    for suppressed in suppressed_list:
        paragragh = paragragh.replace(suppressed, "")
    return paragragh

"""
clean  paragragh

@param: paragragh to clean
@return paragragh after clean
"""
def clean_content(paragragh: str):
    paragragh = paragragh.replace("\n", " ")
    paragragh = paragragh.replace("<", "").replace(">", "").replace("[]", "").replace("[ ]", "")
    paragragh = paragragh.replace('?','.')
    paragragh = paragragh.replace('!','.')
    paragragh = paragragh.replace('。','.')
    paragragh = " ".join(paragragh.split())
    return paragragh

"""
clean list of paragragh

@param paragraghs: list of paragragh to clean
@param suppressed_flag: True if want to clean suppressed, False if not
@return list of paragragh after clean
"""
def clean_document(parapraghs: list, suppressed_flag: bool):
    suppressed_parapraghs = []
    for i in range(len(parapraghs)):
        parapraghs[i] = clean_content(parapraghs[i])
        parapraghs[i] = remove_index_paragraph(parapraghs[i])
        if suppressed_flag:
            if find_suppressed(parapraghs[i]):
                suppressed_parapraghs.append(parapraghs[i])
                suppressed_parapraghs[-1] = clean_suppressed(suppressed_parapraghs[-1])

    if suppressed_flag: return suppressed_parapraghs
    return parapraghs

"""
get number of word in paragragh

@param paragragh: paragragh to count
@return number of word in paragragh
"""
def get_number_of_paragraph(paragraghs: str):
    paragraghs = paragraghs.split(' ')
    return len(paragraghs)

"""
check language of paragragh is english or not

@param paragraghs: list of paragragh to check
@param threshold: number of word to check
@return True if paragragh is english, False if not
"""
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

"""
take the body have language is english

@param bodytop: list of paragragh in bodytop
@param bodybot: list of paragragh in bodybot
@param threshold: number of word to check
@return body of document in english
"""
def choose_body(bodytop: list, bodybot: list, threshold: int):
    lan_top = detect_language(bodytop, threshold)
    lan_bot = detect_language(bodybot, threshold)
    if lan_top:
        body = parsing.parsing_body(bodytop)
    elif lan_bot:
        body = parsing.parsing_body(bodybot)
    else: 
        return ""
    return body

"""
get label of document in label link

@param name: name of document
@param label_link: link to label
@return dictionary of document have label
"""
def run_get_label(name: str, label_link):
    label_list = getlabel.get_label(name, label_link)
    label = len(label_list)
    return {
        "id": name,
        "label": label,
        "label_list": label_list
    }

"""
run preprocessing

@param document: document to preprocessing
@param suppressed_flag: True if want to clean suppressed, False if not
@return dictionary of document after preprocessing
"""
def run_preprocessing(document: str, suppressed_flag: bool):
    parsing_doc = parsing.parsing_document(document)
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
        "year": year,
        "meta": meta,
        "body": body_year,
    }