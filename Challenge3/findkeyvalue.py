def find_value_from_nested_obj(nested_obj, key):
    if isinstance(nested_obj, dict):
        if key in nested_obj:
            return nested_obj[key]
        else:
            for k, v in nested_obj.items():
                result = find_value_from_nested_obj(v, key)
                if result is not None:
                    return result
    elif isinstance(nested_obj, list):
        for item in nested_obj:
            result = find_value_from_nested_obj(item, key)
            if result is not None:
                return result

    return None
nested_obj = {"x": {"y": {"z": "a"}}}
key_to_find =  'y'
result = find_value_from_nested_obj(nested_obj, key_to_find)
print(result)  # Output: value