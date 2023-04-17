import os
import json

def read_jsonfile(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return json.load(f)
    else:
        return []
    
def read_txtfile(filename):
    if os.path.exists(filename):
        with open(filename, 'r', encoding = "utf8") as f:
            return f.read()
    else:
        return ""
    
def get_folder(filename):
    return os.listdir(filename)

def write_jsonfile(filename, data):
    result = json.dumps(data, indent=2, ensure_ascii=False)
    myjsonfile = open(filename, "w", encoding="utf8")
    myjsonfile.write(result)
    myjsonfile.close()