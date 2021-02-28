'''Implementation of the logic for representing the requests and logging them.'''

import datetime
import sqlite3
import pandas as pd
import json
import os

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

    

    

