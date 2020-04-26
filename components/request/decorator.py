import functools
from components.utils.json_util import DictObject, json_to_obj_v2


def json_to_obj_ns(func) -> DictObject:
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        value = func(*args, **kwargs)
        return json_to_obj_v2(value.content)
    return wrapper_decorator
