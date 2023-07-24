def find_value_from_nested_obj(obj, key):
    if isinstance(obj, dict):
        if key in obj:
            return obj[key]
        else:
            for k, v in obj.items():
                result = find_value_from_nested_obj(v, key)
                if result is not None:
                    return result
    elif isinstance(obj, list):
        for item in obj:
            result = find_value_from_nested_obj(item, key)
            if result is not None:
                return result

    return None
obj = {"x": {"y": {"z": "a"}}}
key_to_find =  'y'
result = find_value_from_nested_obj(obj, key_to_find)
print(result)  # Output: value
