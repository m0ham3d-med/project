

def parse(filename):
    Lines = open(filename, 'r').readlines()
    req_number=[]
    for line in Lines :
        if "Cook" in line:
           req_number.append( line.split(":")[1])
    return req_number

def faus_possitive(list_req):
    fp_normal=0
    fp_attack=0
    for i in list_req:
        if i > 300:
            fp_normal+=1
    for i in range(300):
        if i not in list_req:
            fp_attack+=1
    
    return fp_attack,fp_normal


    
            

parse("modsec_audit.log")