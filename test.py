import math



article_text = '''
reated wheel for nltk: filename=nltk-3.5-py3-none-any.whl size=1434676 sha256=758af4ff9a888651d1cdee5d4814347d52bb3caa6ee8a922ace3dffd605ff637
  Stored in directory: /home/med/.cache/pip/wheels/ff/d5/7b/f1fb4e1e1603b2f01c2424dd60fbcc50c12ef918bafc44b155
Successfully built nltk
Installing collected packages: regex, tqdm, nltk
  WARNING: The script tqdm is installed in '/home/med/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The script nltk is installed in '/home/med/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  '''


# s =" < ../ alert exec password <> ’ alter from path/child <!– “ and href script = ( bash_history #include select > ) between insert shell | $ /c into table || * cmd javascript: union - */ cn= mail= upper –> & commit objectclass url= ; + count onmouseover User-Agent: : %00 -craw or where / %0a document.cookie order winnt /* Accept: etc/passwd passwd  "
# req =["/index.php","None","*/* gzip,deflate no-cache close http://192.168.175.220:80/index.php sqlmap/1.2.4#stable (http://sqlmap.org)","4618"]
def preprocess(text):
    text = text.lower()
    text = re.sub(r'\W',' ',text)
    text = re.sub(r'\s+',' ',text)
    return text 

def request_to_bow(req_list):
    total_length  =len(req_list.split()) 
    bag =[]
    words = [ '<', '../', 'alert', 'exec', 'password', '<>', '’', 'alter', 'from', 'path/child', '<!–', '“', 'and', 'href', 'script', '=', '(', 'bash_history', '#include', 'select', '>', ')', 'between', 'insert', 'shell', '|', '$', '/c', 'into', 'table', '||', '*', 'cmd', 'javascript:', 'union', '-', '*/', 'cn=', 'mail=', 'upper', '–>', '&', 'commit', 'objectclass', 'url=', ';', '+', 'count', 'onmouseover', 'User-Agent:', ':', '%00', '-craw', 'or', 'where', '/', '%0a', 'document.cookie', 'order', 'winnt', '/*', 'Accept:', 'etc/passwd', 'passwd', ]
    for item  in words :
        repeat_nbr = req_list.count(item)
        value =  repeat_nbr / total_length
        bag.append(math.floor(value))  
    return bag    



print(request_to_bow(article_text))

