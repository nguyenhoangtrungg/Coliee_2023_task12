### 🆕 Elasticsearch

#### Input:
```json
{
  "id": ,
  "label": ,
  "label_list": ,
  "year": ,
  "meta": ,
  "body": [
	{
		"content": ,
		"year": ,
	},
	...
  ],

  "id": ,
  "label": ,
  "label_list": ,
  "year": ,
  "meta": ,
  "body": [
	{
		"content": ,
		"year": ,
	},
	...
  ]
  ...
}
```

#### Output:


### 🆕 Processing
#### Input:
```
input_folder
├── 000001.txt
├── 000002.txt
├── 000003.txt
```
`000001.txt`
```txt
.......................
.......................
[1]
.......................
[2]
.......................

...

[n]
.......................
```

#### Output:
```
output_folder
├── 000001.json
├── 000002.json
├── 000003.json
```
```json
{
  "id": ,
  "label": ,
  "label_list": ,
  "year": ,
  "meta": ,
  "body": [
	{
		"content": ,
		"year": ,
	},
	...
  ]
}
```

#### Label:
```json
{
    "000001.txt": ["000005.txt", "012101.txt"],
   	"003423.txt": ["398421.txt", "012101.txt", "173651.txt"],
   	"012831.txt": ["000001.txt"],
   	...
}
```