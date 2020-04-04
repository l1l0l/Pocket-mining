from urllib.request import Request
from urllib.request import urlopen
from urllib import parse
from urllib.error import HTTPError
from config import CONSUMER_KEY, ACCESS_TOKEN
import json

REQUEST_URL = "https://getpocket.com/v3/oauth/request"
GET_URL     = "https://getpocket.com/v3/get"

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
    data = {
        'consumer_key': CONSUMER_KEY, 
        'redirect_uri': 'pocketapp1234:authorizationFinished'
    }
    reponse = do_post_request(REQUEST_URL, data)  # byte response
    code = response.decode("utf-8").split('code=')[1]
    return code

def retrieve(**kwargs):
    data = {
        'consumer_key': CONSUMER_KEY, 
        'access_token': ACCESS_TOKEN,
    }
    data.update(kwargs)
    response = do_post_request(GET_URL, data)
    retrieve_result = json.loads(response.decode('utf-8'))
    return retrieve_result

def get_items(retrieve_result):
    return list(reduce(lambda x,y: (x[1],y[1]) if isinstance(x[0],str) else x+(y[1],), \
                                retrieve_result['list'].items()))

def get_items_id(retrieve_result):
    return list(reduce(lambda x,y:(x[0],y[0]) if isinstance(x[-1],dict) else x+(y[0],), \
                          retrieve_result['list'].items()))