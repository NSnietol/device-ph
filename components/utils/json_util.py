
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


class DictObject(object):
    def __init__(self, d):
        for a, b in d.items():
            if isinstance(b, (list, tuple)):
               setattr(self, a, [DictObject(x) if isinstance(x, dict) else x for x in b])
            else:
               setattr(self, a, DictObject(b) if isinstance(b, dict) else b)
    def get_dict(self):
        return dict(self.__dict__.items())

def json_to_obj_latest(data): 
    return DictObject(json.loads(data))


