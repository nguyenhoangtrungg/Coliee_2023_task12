# Coliee task 1 2


## 📦 Installation

Make sure to install the required packages at `requirements.txt`

## 🚀 How to use

### 🆕 Elasticsearch

#### Step 1:

Elastichsearch sử dụng để tìm kiếm các câu trong các văn bản phù hợp với truy vấn. Câu truy vấn bao gồm nội dung và năm.

Start Elasticsearch on your machine.

After that fill your account and password in parameters of function login and information of index in parameters of function indexing, input_link is link of input after preprocessing, link_folder_out is link of result in file `runelasticsearch.py`.

Các bước tiền xử lý được thực hiện trong file `runelasticsearch.py`. Các tham số đầu vào của hàm `runelasticsearch.py` lần lượt có ý nghĩa như sau:

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

Tiền xử lý tập trung vào việc tách các câu ra và làm sạch dữ liệu. Các bước tiền xử lý được thực hiện như sau:

1. Tách các câu ra khỏi văn bản
2. Loại bỏ các ký tự đặc biệt
3. Loại bỏ các từ không cần thiết
4. Loại bỏ các từ trùng lặp
5. Loại bỏ các từ không có ý nghĩa

Các bước tiền xử lý được thực hiện trong file `runpreprocessing.py`. Các tham số đầu vào của hàm `runpreprocessing.py` lần lượt có ý nghĩa như sau:

Run file 

```bash
python runpreprocessing.py -il "input_link" -ll "label_link" -ol "output_link" -fl "flag_suppressed"
```

**Parameters:**
* folder_input_link: link đến thư mục chứa các văn bản
* label_link: link đến file chứa các nhãn
* output_link: link đến file kết quả
* flag_suppressed: cờ để chọn có lọc các câu hay không