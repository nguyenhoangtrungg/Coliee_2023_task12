# Coliee task 1 2


## 📦 Installation

Make sure to install the required packages at `requirements.txt`

## 🚀 How to use

### 🆕 Elasticsearch

Use Elasticsearch to search for sentences in documents that match the query. The query includes the content and the year.

#### Step 1:
Set up your elasticsearch `https://www.elastic.co/guide/en/elasticsearch/reference/current/setup.html`

#### Step 2:
Run Elasticsearch on your machine. Take account and password of Elasticsearch.

#### Step 3:
Run file
```bash
python runelasticsearch.py -acc "account" -pw "password" -ix "index" -il "input_link" -ol "output_link"
```
**Parameters:**
* account: tài khoản của Elasticsearch
* password: mật khẩu của Elasticsearch
* index: tên của index
* input_link: link đến thư mục chứa các văn bản sau khi tiền xử lý
* output_link: link đến thư mục chứa kết quả

Example of data:


### 🆕 Processing

Preprocessing focuses on separating statements and cleaning data. The steps to process money are as follows:

1. Split meta and content
2. Add label (have)
3. Add year in document
4. Separate sentences from text
5. Remove special characters
6. Remove unnecessary words
7. Remove index

#### Step 1: Run file 

Run file with command:

```bash

```bash
python runpreprocessing.py -il "input_link" -ll "label_link" -ol "output_link" -fl "flag_suppressed"
```

**Parameters:**
* folder_input_link: link to the folder containing the documents
* label_link: link to the file containing the labels
* output_link: link to the output file
* flag_suppressed: flags to select the filter of the question or not