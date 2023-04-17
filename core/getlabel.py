import readfile

def list_label(link):
    label_list = readfile.read_jsonfile(link)
    return label_list

def get_label(index, label_list):
    try:
        return label_list[index]
    except:
        return []
    
def get_label_from_file(index, label_list):
    if label_list == []: return []
    return get_label(index, label_list)