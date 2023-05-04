import readfile
import matplotlib.pyplot as plt

def get_key(label):
    return list(label.keys())

def get_value(key, label):
    return len(label[key])

def get_list_key_value(label):
    ls_key = get_key(label)
    ls_value = []
    for key in ls_key:
        ls_value.append(get_value(key, label))
    return ls_value

def get_statistical(label):
    ls_value = get_list_key_value(label)
    max_value = max(ls_value)
    min_value = min(ls_value)
    sum_value = sum(ls_value)
    avg_value = sum_value/len(ls_value)
    return {
        "len": len(ls_value),
        "min": min_value,
        "max": max_value,
        "avg": avg_value
    }

def plot_statistical(label):
    ls_value = get_list_key_value(label)
    plt.hist(ls_value, bins=100)
    plt.show()

label = readfile.read_jsonfile("D:\Lab\Coliee_2023_task12\data\\task1_test_labels_2023.json")
ls_key = get_key(label)
print(get_statistical(label))

plot_statistical(label)
