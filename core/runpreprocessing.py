import getyear
import preprocessing
import readfile

"""
run function to parse all documents in folder 
@param folder_link: link to folder contain all documents
@param label_link: link to file contain all labels
@param suppress_flag: flag to suppress the document
@return list of document after parsing
"""
def run(folder_link, label_link, suppress_flag: bool):
    output = []
    folder = readfile.get_folder(folder_link)
    label_list = readfile.read_jsonfile(label_link)
    for link in folder:
        document = readfile.read_txtfile(folder_link + "\\" + link)
        if document == "": continue
        header = preprocessing.run_get_label(link, label_list)
        body = preprocessing.run_preprocessing(document, suppress_flag)
        full_text = {
            "id": header["id"],
            "label": header["label"],
            "label_list": header["label_list"],
            "year": body["year"],
            "meta": body["meta"],
            "body": body["body"]
        }
        output.append(full_text)
    return output

"""
@param folder_input_link: link to folder contain all documents
@param label_link: link to file contain all labels
@param output_link: link to output file
@param flag_suppressed: flag to suppress the document
@return result to output file
"""
if __name__ == '__main__':
    folder_input_link = "D:\Lab\Coliee_2023_task12\data"
    label_link = "D:\Lab\Coliee_2023_task12\\task1_train_labels_2023.json"
    output_link = "demo.json"
    flag_suppressed = False
    output = run(folder_input_link, label_link, flag_suppressed)
    readfile.write_jsonfile(output_link, output)