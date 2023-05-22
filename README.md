# Coliee task 1 2 - check duplicate

## 📦 Installation

Make sure to install the required packages at `requirements.txt`

## 🚀 How to use

### 🆕 Processing

Preprocessing focuses on separating statements and cleaning data. The steps to preprocessing are as follows:

1. Split meta and content
2. Add label (optional)
3. Add year in document
4. Separate sentences from text
5. Remove special characters
6. Remove unnecessary words
7. Remove index

#### Step 1: Run file 

Run file with command:

```bash
python runpreprocessing.py --input_path "input_path" --label_path "label_path" --output_path "output_path" --flag_suppressed "flag_suppressed"
```

**Parameters:**
* input_path: path to the folder containing the documents. Default value: "data\input"
* label_path: path to the file containing the labels. Default value: "data\\task1_train_labels_2023.json"
* output_path: path to the output file. Default value: "data\output"
* flag_suppressed: flag if keep only paragraph have keyword "_suppressed". Default value: 0

**Note**:
If a parameter is not provided, the default value will be used.

### 🆕 Elasticsearch

Use Elasticsearch to search for sentences in documents that match the query. The query includes the content and the year.

#### Step 1:
Set up your elasticsearch `https://www.elastic.co/guide/en/elasticsearch/reference/current/setup.html`

#### Step 2:
Run Elasticsearch on your machine. Take account and password of Elasticsearch.

#### Step 3:
Run file
```bash
python runelasticsearch.py --account "account" --password "password" --index "index" --mode = "mode" --input_path "input_path" --output_path "output_path"
```
**Parameters:**
* account: Elasticsearch's account. Default value: "elastic"
* password: Elasticsearch password. Default value: "123456"
* index: name of the index. Default value: "es_coliee"
* mode: run mode have 3 bits corresponding mapping, indexing, searching with bit 1 is turn on mode. Default value: "111"
* input_path: path to the directory containing the preprocessed text. Default value: "\data\output"
* output_path: path to the directory containing the results. Default value: "\data\es_output"

**Note**:
If a parameter is not provided, the default value will be used.

### 🆕 Check duplicate

Check duplicate document in corpus

#### Step 1: Run file

Run file with command:

```bash
python runcheckduplicate.py --input_path "input_path" --output_path "output_path"
```

**Parameters:**
* input_path: path to the folder containing the documents. Default value: "data\es_output"
* output_path: path to the output file. Default value: "data\output"

**Note**:
If a parameter is not provided, the default value will be used.
