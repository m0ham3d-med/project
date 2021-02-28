'''Defines a class for threat classification.
This class impelemnts some methods for cleaning of the inputs and uses trained classifiers for prediction.'''

from sklearn.externals import joblib
from request import Request
import urllib.parse
import json

class Classifier(object):
    def __unquote(self, text):
        k = 0
        uq_prev = text
        while(k < 100):
            uq = urllib.parse.unquote_plus(uq_prev)
            if uq == uq_prev:
                break
            else:
                uq_prev = uq
    
        return uq_prev

    def __remove_new_line(self, text):
        text = text.strip()
        return ' '.join(text.splitlines())

    def __remove_multiple_whitespaces(self, text):
        return ' '.join(text.split())

    def __clean_pattern(self, pattern):
        pattern = self.__unquote(pattern)
        pattern = self.__remove_new_line(pattern)
        pattern = pattern.lower()
        pattern = self.__remove_multiple_whitespaces(pattern)

        return pattern

    def __is_valid(self, parameter):
        return parameter != None and parameter != ''
    
    
    # def get_cookie(self,headers):
        # return headers.pop("Cookie")

    def get_cookie_value(self,cookies):
        ck = cookies.split(";")
        value = []
        for a in ck:
            val = a.split("=")
            val.pop(0)
            value.append(" ".join(val))

        return " ".join(value)

    def get_parameter(self,body):
        if self.__is_valid(body):
            request_parameters = urllib.parse.parse_qs(self.__clean_pattern(req.request))
 
    # def get_path_parameter(self,text):
        # request_parameters = urllib.parse.parse_qs(text)
        # param = []
        # for i in request_parameters :
        #     param.append(" ".join(request_parameters[i]))
        # return " ".join(param)
        # print(text)

    def get_stream_parameter(self,text):
        request_parameters = urllib.parse.parse_qs(text)
        param = []
        for i in request_parameters :
            param.append(" ".join(request_parameters[i]))
        return " ".join(param)

    def get_json_parameter(self,json_data):
        param = []
        for key in json_data :
            param.append(" ".join(json_data[key]))
        return " ".join(param)

    def get_path (self,path):
        spl =path.split("?",1)
        path =spl[0]
        if len(spl) == 2 :
            parameters =spl[1]
        else:
            parameters = None
        return path, parameters

    def get_headers_value(self,headers):
        value = []
        for header in headers:
            value.append(headers[header])
        return " ".join(value)


    def classify_request(self, req):
        if not isinstance(req, Request):
            raise TypeError("Object should be a Request!!!")
               
        parameters = []
        path ,params = self.get_path(req.request)
    
        ###  get path
        if self.__is_valid(path):
           parameters.append(self.__clean_pattern(path))
            
        #### get cookies
        if 'Cookie' in req.headers and self.__is_valid(req.headers['Cookie']):
            req.cookies = req.headers.pop("Cookie")
            parameters.append(self.__clean_pattern(self.get_cookie_value(req.cookies)))
        else:
            parameters.append(None)
                

        
        ###### get headers
        if self.__is_valid(req.headers) and isinstance(req.headers, dict) :
            headers = self.get_headers_value(req.headers)
            parameters.append(self.__clean_pattern(headers))
        
        #####get parameters
        if self.__is_valid(req.body):
            if isinstance(req.body, dict): 
                parameters.append(self.__clean_pattern(self.get_json_parameter(req.body)))
            else:
                parameters.append(self.__clean_pattern(self.get_stream_parameter(req.body)))
        if self.__is_valid(params):
            parameters.append(self.__clean_pattern(self.get_stream_parameter(params)))
        
    

        
        

        print(parameters)
        return(parameters)


