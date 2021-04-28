from xml.etree import ElementTree as ET
import base64
from urllib.parse import unquote
#
    
def a(row):
        all=[]
        tree = ET.parse(row)
        root = tree.getroot()
        for reqs in root.findall('item'):
            raw_req = reqs.find('request').text
            try:
                request=base64.b64decode(raw_req)
                request=request.decode('utf-8')
                with open('{}.txt'.format(row), 'a') as writter:
                    writter.write(request)                
            except:
                pass

            # all.append(request)

       

		# return result

a("raw")

