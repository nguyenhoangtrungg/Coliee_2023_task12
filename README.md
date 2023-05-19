# Coliee task 1 2 - check duplicate


## 📦 Installation

Make sure to install the required packages at `requirements.txt`

## 🚀 How to use

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
python runpreprocessing.py --input_link "input_link/defaul" --label_link "label_link/defaul" --output_link "output_link/defaul" --flag_suppressed "flag_suppressed/defaul"
```

**Parameters:**
* folder_input_link: link to the folder containing the documents
* label_link: link to the file containing the labels
* output_link: link to the output file
* flag_suppressed: flag if keep only paragraph have keyword "_suppressed"

**Note**:
If dont fill parameter , it will be left as default

### 🆕 Elasticsearch

Use Elasticsearch to search for sentences in documents that match the query. The query includes the content and the year.

#### Step 1:
Set up your elasticsearch `https://www.elastic.co/guide/en/elasticsearch/reference/current/setup.html`

#### Step 2:
Run Elasticsearch on your machine. Take account and password of Elasticsearch.

#### Step 3:
Run file
```bash
python runelasticsearch.py --account "account/defaul" --password "password/defaul" --index "index/defaul" --mode = "mode/defaul" --input_link "input_link/defaul" --output_link "output_link/defaul"
```
**Parameters:**
* account: Elasticsearch's account
* password: Elasticsearch password
* index: name of the index
* mode: run mode have 3 bits corresponding mapping, indexing, searching with bit 1 is turn on mode
* input_link: link to the directory containing the preprocessed text
* output_link: link to the directory containing the results

**Note**:
If dont fill parameter , it will be left as default

### 🆕 Check duplicate

Check duplicate document in corpus

#### Step 1: Run file

Run file with command:

```bash
python runcheckduplicate.py --inputpath "input_link/defaul" --outputpath "output_link/defaul"
```

**Parameters:**
* input_link: link to the folder containing the documents
* output_link: link to the output file

**Note**:
If dont fill parameter , it will be left as default

## Citations  

```bash
  title = {},
  author = {Thi-Hai-Yen Vuong, Hai-Long Nguyen, Tan-Minh Nguyen, Hoang-Trung Nguyen, Thai-Binh Nguyen and Ha-Thanh Nguyen},
  booktitle = {},
  year = {2023},
```