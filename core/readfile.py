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
        with open(filename, 'r') as f:
            return f.read()
    else:
        return ""
    
def get_folder(filename):
    return os.path.dirname(filename)