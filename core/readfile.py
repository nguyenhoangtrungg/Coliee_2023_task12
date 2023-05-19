import os
import json

"""
@param filename: path to file
@return: content in json file
"""
def read_jsonfile(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return json.load(f)
    else:
        return []

"""
@param filename: path to file
@return: content in txt file
"""
def read_txtfile(filename):
    if os.path.exists(filename):
        with open(filename, 'r', encoding = "utf8") as f:
            return f.read()
    else:
        return ""
    
"""
@param filename: path to file
@return: list of file in folder
"""
def get_folder(filename):
    return os.listdir(filename)

"""
write data to json file

@param filename: path to file
@param data: data to write
"""
def write_jsonfile(filename, data):
    result = json.dumps(data, indent=2, ensure_ascii=False)
    myjsonfile = open(filename, "w", encoding="utf8")
    myjsonfile.write(result)
    myjsonfile.close()