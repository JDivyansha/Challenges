def get_value(obj, key):
    keys = key.split('/')

    def traverse(obj, keys):
        if len(keys) == 0:
            return obj

        if keys[0] in obj:
            return traverse(obj[keys[0]], keys[1:])
        else:
            return None

    return traverse(obj, keys)

# Input
obj ={"x": {"y": {"z": "a"}}}
key = 'x/y'

#Output
value = get_value(obj, key)
print(value) 
