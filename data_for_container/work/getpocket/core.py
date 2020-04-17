def relation(json_from, json_to):
    if not isinstance(json_to, dict):
            return 'attribute' +
    all_items_are_dict = True
    keys=[]; values=[]
    for k,v in json_to.items():
        keys.append(k); values.append(v)
        if not isinstance(v, dict):
            all_items_are_dict = False
            return 'ONE_TO_ONE'
    if all_items_are_dict:
        # tester si tous les clés sont des entiers
        all_keys_are_numbers = True
        for k in keys: 
            if not any(map(str.isdigit, k)):
                all_keys_are_numbers = False
        if all_keys_are_numbers:
            return 'ONE_TO_MANY'
        else:
            return 'attribute(list)?'
        
def model(json):
     for k,v in json.items():
            print("+", k, ":" ,relation(json, v))


def process_likeness(key, subclass_name):
    return 0.5

def subclass_from_key(key, base_class):
    for subclass in base_class.__subclasses__():
        process_likeness(key, subclass.__name__)
        

