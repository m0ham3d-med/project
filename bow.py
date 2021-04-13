
import csv


def add_to_csv_file(filename,data):
    with open(filename, 'a+', newline='') as out:
            file_write = csv.writer(out, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            file_write.writerow(data)

def request_to_bow(text):
        text =text.lower()
        total_length  = len(text.split()) 
        if total_length  == 0 :
            return [0] * 64
        bag =[]
        words = [ '<', '../', 'alert', 'exec', 'password', '<>', '’', 'alter', 'from', 'path/child', '<!–', '“', 'and', 'href', 'script', '=', '(', 'bash_history', '#include', 'select', '>', ')', 'between', 'insert', 'shell', '|', '$', '/c', 'into', 'table', '||', '*', 'cmd', 'javascript:', 'union', '-', '*/', 'cn=', 'mail=', 'upper', '–>', '&', 'commit', 'objectclass', 'url=', ';', '+', 'count', 'onmouseover', 'User-Agent:', ':', '%00', '-craw', 'or', 'where', '/', '%0a', 'document.cookie', 'order', 'winnt', '/*', 'Accept:', 'etc/passwd', 'passwd', ]
        for item  in words :
            repeat_nbr = text.count(item)
            value =  repeat_nbr / total_length
            bag.append(value)
        return bag 



file1 = open("datsets/global_dataset.csv", "r")
csv_filename = "datsets/ml_dataset.csv"

for line in file1:
    bag = request_to_bow(str(line))
    if "attack" in line:
        bag.append(1)
    else:
        bag.append(0)
    add_to_csv_file(csv_filename,bag)
    
file1.close()

