


def numerise(file1,file2):
    Lines = open(file1, 'r').readlines()
    request_number=0
    for line in Lines :
        header="Request_number: {}".format(request_number)
        # line = line.replace("\n", "")
        with open(file2, 'a') as writter:
                    writter.write("{}".format(line))
        if "Host: " in line :
            with open(file2, 'a') as writter:
                    writter.write("{}\n".format(header))
                    request_number+=1

    return 0
                            
numerise("raw.txt","finale.txt")                                        
       