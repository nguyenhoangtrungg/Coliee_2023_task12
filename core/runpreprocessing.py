import preprocessing
import readfile
import argparse

"""
run function to parse all documents in folder 
@param folder_path: path to folder contain all documents
@param label_path: path to file contain all labels
@param suppress_flag: flag if keep only paragraph have keyword suppress
@return list of document after parsing
"""
def run(folder_path, label_path, output_path, suppress_flag: bool):
    output = []
    folder = readfile.get_folder(folder_path)
    label_list = readfile.read_jsonfile(label_path)
    for path in folder:
        document = readfile.read_txtfile(folder_path + "\\" + path)
        if document == "": continue
        header = preprocessing.run_get_label(path, label_list)
        print(path)
        body = preprocessing.run_preprocessing(document, suppress_flag)
        full_text = {
            "id": header["id"],
            "label": header["label"],
            "label_list": header["label_list"],
            "year": body["year"],
            "meta": body["meta"],
            "body": body["body"]
        }
        local_id = header["id"].split(".")[0]
        local_output_path = output_path + "\\" + local_id + ".json"
        readfile.write_jsonfile(local_output_path, full_text)
    return output

"""
@param input_path: path to folder contain all documents
@param label_path: path to file contain all labels
@param output_path: path to output file
@param flag_suppressed: flag if keep only paragraph have keyword suppress
@return result to output file
"""
if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Data Processing.')

    parser.add_argument("-il", "--inputpath", help="path folder of input.", default="data\input", type=str)
    parser.add_argument("-ll", "--labelpath", help="path of label.", default="data\\task1_train_labels_2023.json", type=str)
    parser.add_argument("-ol", "--outputpath", help="path of output.", default="data\output", type=str)
    parser.add_argument("-fl", "--flag_suppressed", help="flag.", default=0, type=int)

    args = parser.parse_args()    

    folder_input_path = args.inputpath
    label_path = args.labelpath
    output_path = args.outputpath
    flag_suppressed =  args.flag_suppressed
    if flag_suppressed == 0:
        flag_suppressed = False
    else: 
        flag_suppressed = True
    output = run(folder_input_path, label_path, output_path, flag_suppressed)