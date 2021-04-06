import csv


def read_cisc_row(filename ):
    Lines = open(filename, 'r').readlines()
    array = []
    req = []
    for line in Lines :
        line = line.replace("\n", "")
        if "POST " in line or "GET " in line:
            array.append(" ".join(req))
            line = line.split(" ")[1]
            req = []
            req.append(line)
        else :
            if ":" in line :
                line = line.split(":")[1]
            req.append(line)
    return array

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



csv_filename  = "cis_dataset.csv"
cisc_filename = "anomalousTrafficTest.txt"
request_list =read_cisc_row(cisc_filename)

for req in request_list :
    bag=[]
    bag.append (str(req))
    bag.append("attack")
    # bag = request_to_bow(str(req))
    # bag.append(0)
    add_to_csv_file(csv_filename,bag)

