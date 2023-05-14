# Coliee task 1 2


## 📦 Installation

Make sure to install the required packages at `requirements.txt`

## 🚀 How to use

### 🆕 Elasticsearch

Start Elasticsearch on your machine.

After that fill your account and password in parameters of function login and information of index in parameters of function indexing, input_link is link of input after preprocessing, link_folder_out is link of result in file `runelasticsearch.py`.

This is a example:

```python
acount = "elastic"
password = "TfO2an_x*5qCiwBcoAdE"

_index = "es_coliee_test"
input_link = "\data\output\\test_querylist.json"
link_folder_out = "\demo\\"
```

Run file runelasticsearch.py

```python
client = login(acount, password)
mapping(client, _index)
indexing(client, _index, input_link)

write_data(input_link, link_folder_out)
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

This is a example:

```python
folder_input_link = "\data\input"
label_link = "\\task1_train_labels_2023.json"
output_link = "demo.json"
flag_suppressed = False
```

Run file runpreprocessing.py

```python
output = run(folder_input_link, label_link, flag_suppressed)
readfile.write_jsonfile(output_link, output)
```