import readfile

"""
take list of labels from file

@param link: link to file contain all labels
@return list of labels
"""
def list_label(link):
    label_list = readfile.read_jsonfile(link)
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
@param label_list: link to file contain all labels
@return list have label, return empty list if not found
"""
def get_label_from_file(index, label_list):
    if label_list == []: return []
    return get_label(index, label_list)