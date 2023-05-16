# Coliee task 1 2


## 📦 Installation

Make sure to install the required packages at `requirements.txt`

## 🚀 How to use

### 🆕 Elasticsearch

Start Elasticsearch on your machine.

After that fill your account and password in parameters of function login and information of index in parameters of function indexing, input_link is link of input after preprocessing, link_folder_out is link of result in file `runelasticsearch.py`.

Run file

`python runelasticsearch.py -acc "account" -pw "password" -ix "index" -il "input_link" -ol "output_link"`

```python
parser = argparse.ArgumentParser(description='Elasticsearch.')

parser.add_argument("-acc", "--account", help="Account of Elasticsearch.", default="elastic", type=str)
parser.add_argument("-pw", "--password", help="Password of Elasticsearch.", default=None, type=str)
parser.add_argument("-ix", "--index", help="Index name.", default="es_coliee", type=str)
parser.add_argument("-il", "--input_link", help="link of input", default="data/input", type=str)
parser.add_argument("-ol", "--output_link", help="link of folder output.", default="data/output", type=str)

args = parser.parse_args()

account = args.account
password = args.password
_index = args.index

input_link = args.input_link
output_link = args.output_link

client = login(account, password)
mapping(client, _index)
indexing(client, _index, input_link)

write_data(input_link, output_link)
```

### 🆕 Processing

Tiền xử lý tập trung vào việc tách các câu ra và làm sạch dữ liệu. Các bước tiền xử lý được thực hiện như sau:

1. Tách các câu ra khỏi văn bản
2. Loại bỏ các ký tự đặc biệt
3. Loại bỏ các từ không cần thiết
4. Loại bỏ các từ trùng lặp
5. Loại bỏ các từ không có ý nghĩa

Các bước tiền xử lý được thực hiện trong file `preprocessing.py`. Các tham số đầu vào của hàm `run` bao gồm:
folder_input_link, label_link, output_link, flag_suppressed lần lượt có ý nghĩa như sau:

* folder_input_link: link đến thư mục chứa các văn bản
* label_link: link đến file chứa các nhãn
* output_link: link đến file kết quả
* flag_suppressed: cờ để chọn có lọc các câu hay không

Run file 

`python runpreprocessing.py -il "input_link" -ll "label_link" -ol "output_link" -fl "flag_suppressed"`

```python
parser = argparse.ArgumentParser(description='Data Processing.')

parser.add_argument("-il", "--input_link", help="link folder of input.", default="data/input", type=str)
parser.add_argument("-ll", "--label_link", help="link of label.", default="data/label", type=str)
parser.add_argument("-ol", "--output_link", help="link of output.", default="data/output", type=str)
parser.add_argument("-fl", "--flag_suppressed", help="flag.", default=False, type=bool)

args = parser.parse_args()

folder_input_link = args.input_link
label_link = args.label_link
output_link = args.output_link
flag_suppressed =  args.flag_suppressed
output = run(folder_input_link, label_link, flag_suppressed)
readfile.write_jsonfile(output_link, output)
```