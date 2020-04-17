from urllib.request import Request
from urllib.request import urlopen
from urllib import parse
from urllib.error import HTTPError
import json
from functools import reduce
import types
from config import CONSUMER_KEY, ACCESS_TOKEN
import pudb
from core import *

REQUEST_URL = "https://getpocket.com/v3/oauth/request"
GET_URL     = "https://getpocket.com/v3/get"

"""
    je vais essayer de le faire interactivement
""" 
class Pocket:
    
    def __init__(self, **kwargs):
        for k,v in kwargs.items():
            if not isinstance(v, dict):
                setattr(self, k, v)
            else:
                relation = relation(kwargs, v)
                setattr(self, k, Element(**v))

class Element:
    
    def __build__(self, key, **kwargs):
        if key in ('tags',):
            pass
        if key in ('authors'):
            pass
    
    def __init__(self, **kwargs):
        for k,v in kwargs.items():
            if not isinstance(v, dict):
                setattr(self, k, v)
            else:
                ref_to = self.__build__(k, **v)
            """
            elif "tags" in k:
                tags = []
                for k1,v1 in v.items():
                    tag = Tag(k1)
                    tags.append(tag)
                setattr(self, k, tags)
            """
                
    @classmethod
    def from_json(cls, json_string):
        return cls(**json_string)
    
    def __repr__(self):
        result = ("L'objet Page a pour attributs:\n")
        for attr in self.__dir__():
            attr_type = type(getattr(self, attr))
            if  attr_type != types.MethodType and not '____' in attr[:2]+attr[-2:]:
                result = result + ("\t{} = {}\n".format( attr, getattr(self, attr)))
        return result


    

class Page(Element): 
    pass
    
    

class Tag(Element):
    
    def __init__(self, name):
        self.name = name
            
    def __repr__(self):
        #print(self.name)
        return self.name
        

def do_post_request(url, data):
    
    data = parse.urlencode(data).encode()
    request = Request(url=url, data=data)
    try:
        http_response = urlopen(request)
    except HTTPError as e:
        print(e.headers.as_string())
    if http_response:
        text_response = http_response.read()
        return text_response
    

def get_request_token():
    """
        return the REQUEST TOKEN to begin the Pocket authorization process as a str
    """
    data = {
        'consumer_key': CONSUMER_KEY, # pass it as a parameter?
        'redirect_uri': 'pocketapp1234:authorizationFinished'
    }
    response = do_post_request(REQUEST_URL, data)  # byte response
    code = response.decode("utf-8").split('code=')[1]
    return code


def retrieve(**kwargs):
    """
        return the json response of the retrieve request
        optional parameters : state(str), favorite(0 or 1), tag(str), contentType(str), sort(str), 
        detailType(str), search(str), domain(str), since(str), count(int), offset(int)
    """
    data = {
        'consumer_key': CONSUMER_KEY, 
        'access_token': ACCESS_TOKEN,
    }
    data.update(kwargs)
    response = do_post_request(GET_URL, data)
    retrieve_result = json.loads(response.decode('utf-8'))
    return retrieve_result

def _get_keys(given_dict):
    keys = []
    for k,v in given_dict.items():
        keys.append(k)
    return keys
           

def _get_items(retrieve_result):
    
    return list(reduce(lambda x,y: (x[1],y[1]) if isinstance(x[0],str) else x+(y[1],), \
                                retrieve_result['list'].items()))


def _get_items_id(retrieve_result):
    
    return list(reduce(lambda x,y:(int(x[0]),int(y[0])) if isinstance(x[-1],dict) else x+(y[0],), \
                          retrieve_result['list'].items()))


def retrieve_items(retrieve_result=None, **kwargs):
    
    if not retrieve_result: 
        retrieve_result = retrieve(**kwargs)
    if len(retrieve_result['list'].items()) == 1:
        for k,v in retrieve_result['list'].items():
            return v
    return _get_items(retrieve_result)


def retrieve_items_id(retrieve_result=None, **kwargs):
    
    if not retrieve_result: 
        retrieve_result = retrieve(**kwargs)
    if len(retrieve_result['list'].items()) == 1:
        for k,v in retrieve_result['list'].items():
            return k
    return _get_items(retrieve_result)


def is_json_list(json_string):
    pass

def key_list(json_string):
    keys = []
    for k,v in json_string.items():
        keys.append(k)
    return keys

def value_list(json_string):
    values = []
    for k,v in json_string.items():
        values.append(v)
    return values