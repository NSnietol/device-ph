
import json
from collections import namedtuple

def obj_to_json(obj):
    if hasattr(obj, '__dict__'):
        return json.dumps(obj.__dict__)
    else: return json.dumps(obj)

def json_to_obj_v2(data): 
    if(type(json.loads(data))==list):
        return [DictObject(element) for element in json.loads(data)]
    return DictObject(json.loads(data))

class DictObject(object):
    def __init__(self, d):
        for a, b in d.items():
            if isinstance(b, (list, tuple)):
               setattr(self, a, [DictObject(x) if isinstance(x, dict) else x for x in b])
            else:
               setattr(self, a, DictObject(b) if isinstance(b, dict) else b)
    def get_dict(self):
        return dict(self.__dict__.items())
    def __str__(self):
        return str(self.__dict__.items())


