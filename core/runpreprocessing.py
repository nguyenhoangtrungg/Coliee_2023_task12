import preprocessing
import readfile
import argparse

parser = argparse.ArgumentParser(description='Data Processing.')

parser.add_argument("-il", "--input_link", help="link folder of input.", default="\data\input", type=str)
parser.add_argument("-ll", "--label_link", help="link of label.", default="\label\\task1_train_labels_2023.json", type=str)
parser.add_argument("-ol", "--output_link", help="link of output.", default="\data\output", type=str)
parser.add_argument("-fl", "--flag_suppressed", help="flag.", default=False, type=bool)

args = parser.parse_args()

"""
run function to parse all documents in folder 
@param folder_link: link to folder contain all documents
@param label_link: link to file contain all labels
@param suppress_flag: flag to suppress the document
@return list of document after parsing
"""
def run(folder_link, label_link, output_link, suppress_flag: bool):
    output = []
    folder = readfile.get_folder(folder_link)
    label_list = readfile.read_jsonfile(label_link)
    for link in folder:
        document = readfile.read_txtfile(folder_link + "\\" + link)
        if document == "": continue
        header = preprocessing.run_get_label(link, label_list)
        print(link)
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
        local_output_link = output_link + "\\" + local_id + ".json"
        readfile.write_jsonfile(local_output_link, full_text)
        # output.append(full_text)
    return output

"""
@param folder_input_link: link to folder contain all documents
@param label_link: link to file contain all labels
@param output_link: link to output file
@param flag_suppressed: flag to suppress the document
@return result to output file
"""
if __name__ == '__main__':
    folder_input_link = args.input_link
    label_link = args.label_link
    output_link = args.output_link
    flag_suppressed =  args.flag_suppressed
    output = run(folder_input_link, label_link, output_link, flag_suppressed)
    # readfile.write_jsonfile(output_link, output)