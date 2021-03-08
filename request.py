'''Implementation of the logic for representing the requests and logging them.'''

import datetime
import sqlite3
import pandas as pd
import json
import os
import urllib.parse



class Request(object):
    def __init__(self, id = None, timestamp = None, origin = None, host = None, request = None, body = None, method = None, headers = None,cookies = None, threats = None):
        self.id = id
        self.timestamp = timestamp
        self.origin = origin
        self.host = host
        self.request = request
        self.body = body
        self.methbood = method
        self.headers = headers
        self.cookies = cookies
        self.threats = threats


    def to_json(self):
        output = {}

        if self.request != None and self.request != '':
            output['request'] = self.request

        if self.body != None and self.body != '':
            output['body'] = self.body

        if self.headers != None:
            for header, value in self.headers.items():
                output[header] = value

        return json.dumps(output)


class PreprocessRequest(object):
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
 
        json_req = {}
        json_req["path"]   = paramters[0]
        json_req["cookies"]= paramters[1]
        json_req["headers"]= paramters[2]
        json_req["params"] = paramters[3]
        json_req["state"]  = paramters[4]
        
        return json_req
        
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
    

    def request_to_bow(self,req_list):
        text =" ".join(req_list)
        total_length  =len(text.split()) 
        bag =[]
        words = [ '<', '../', 'alert', 'exec', 'password', '<>', '’', 'alter', 'from', 'path/child', '<!–', '“', 'and', 'href', 'script', '=', '(', 'bash_history', '#include', 'select', '>', ')', 'between', 'insert', 'shell', '|', '$', '/c', 'into', 'table', '||', '*', 'cmd', 'javascript:', 'union', '-', '*/', 'cn=', 'mail=', 'upper', '–>', '&', 'commit', 'objectclass', 'url=', ';', '+', 'count', 'onmouseover', 'User-Agent:', ':', '%00', '-craw', 'or', 'where', '/', '%0a', 'document.cookie', 'order', 'winnt', '/*', 'Accept:', 'etc/passwd', 'passwd', ]
        for item  in words :
            repeat_nbr = text.count(item)
            value =  repeat_nbr / total_length
            bag.append(value)
        return bag 


    def process(self, req):
        if not isinstance(req, Request):
            raise TypeError("Object should be a Request!!!")
               
        parameters = []
        path ,params = self.get_path(req.request)
    
        ###  get path
        if self.__is_valid(path):
           parameters.append(str(self.__clean_pattern(path)))
            
        #### get cookies
        if 'Cookie' in req.headers and self.__is_valid(req.headers['Cookie']):
            req.cookies = req.headers.pop("Cookie")
            parameters.append(str(self.__clean_pattern(self.get_cookie_value(req.cookies))))
        else:
            parameters.append("None")
                

        
        ###### get headers
        if self.__is_valid(req.headers) and isinstance(req.headers, dict) :
            headers = self.get_headers_value(req.headers)
            parameters.append(str(self.__clean_pattern(headers)))
        
        #####get parameters
        if self.__is_valid(req.body):
            if isinstance(req.body, dict): 
                parameters.append(str(self.__clean_pattern(self.get_json_parameter(req.body))))
            else:
                parameters.append(str(self.__clean_pattern(self.get_stream_parameter(req.body))))
        if self.__is_valid(params):
            parameters.append(str(self.__clean_pattern(self.get_stream_parameter(params))))
        
    

        
        
        data = self.request_to_bow(parameters)
        data.append("0")
        return data



    
    

