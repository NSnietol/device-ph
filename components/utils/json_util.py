
import json
from collections import namedtuple



def _json_object_hook(d): 
    return namedtuple('Value', d.keys())(*d.values())

def obj_to_json(obj):
    if hasattr(obj, '__dict__'):
        return json.dumps(obj.__dict__)
    else: return json.dumps(obj)

def request_to_obj(request):
    return json.loads(request.text, object_hook=_json_object_hook)

def json_to_obj(data): 
    return json.loads(data, object_hook=_json_object_hook)

