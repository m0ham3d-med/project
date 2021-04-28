import requests


def read_cisc_row(filename ):
    Lines = open(filename, 'r').readlines()
    method=""
    cookies={}
    headers={}
    data=""
    uri=""
    
    for line in Lines :
        line = line.replace("\n", "")
        if "POST " in line or "GET " in line:
            method =line.split(" ")[0]
            if line.split(" ")[1] != "HTTP/1.1":
                uri=line.split(" ")[1]
            
        else :
            if not ":" in line :
                data=line
            elif "Cookie" in line :
                line = line.split(":")
                for cook in line[1].split(";"):
                    a=cook.split("=")
                    b=a.pop(0)
                    a='='.join([str(elem) for elem in a])
                    cookies[str(b)]=str(a)
            
            else:
                if line != '':
                    a=line.split(":")
                    b=a.pop(0)   
                    a=':'.join([str(elem) for elem in a])    
                    a=a[:0] + "" + a[1:]           
                    headers[str(b)]=str(a)


    # Prepare and send request
    req = requests.Request(
        method='GET',
        url="http://localhost{}".format(uri),
        headers=headers,
        data=data,
        cookies=cookies,
    )
    prepared_req = req.prepare()
    session = requests.Session()
    resp = session.send(prepared_req)
    print(resp.status_code)
    print(resp.text)
    print(resp.headers)

read_cisc_row("req.txt")