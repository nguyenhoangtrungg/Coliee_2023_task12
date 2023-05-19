import readfile

"""
take list of labels from file

@param path: path to file contain all labels
@return list of labels
"""
def list_label(path):
    label_list = readfile.read_jsonfile(path)
    return label_list

"""
find label of document with id-index

@param index: index of label
@param label_list: list of labels
@return list have label, return empty list if not found
"""
def get_label(index, label_list):
    try:
        return label_list[index]
    except:
        return []
    
"""
find label of document with id-index from file

@param index: index of label
@param label_list: path to file contain all labels
@return list have label, return empty list if not found
"""
def get_label_from_file(index, label_list):
    if label_list == []: return []
    return get_label(index, label_list)