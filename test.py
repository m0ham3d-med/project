from csv import reader
import csv

# open file in read mode
with open('./dataset.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    # Iterate over each row in the csv using reader object
    
    for row in csv_reader:
        list=[]
        state=row.pop()
        # print(row)
        s = ' '.join([str(elem) for elem in row])
        list.append(s)
        list.append(state)
        with open("dataset3.csv", 'a+', newline='') as out:
            file_write = csv.writer(out, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            file_write.writerow(list)
        # print(list)
        