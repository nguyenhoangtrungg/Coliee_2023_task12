import getyear
import newpreprocessing


# read file
with open('D:\Lab\Coliee_2023_task12\data\\000028.txt', 'r') as myfile:
    data = myfile.read()

print(newpreprocessing.run_preprocessing(data, True))