import json

def find_value_for_key(json_obj, target_key):
    """
    Recursively search for a key in a JSON object and return its value.
    
    :param json_obj: The JSON object (dict or list).
    :param target_key: The key to search for.
    :return: The value associated with the key or None if the key is not found.
    """
    if isinstance(json_obj, dict):
        if target_key in json_obj:
            return json_obj[target_key]
        for key, value in json_obj.items():
            result = find_value_for_key(value, target_key)
            if result is not None:
                return result
    elif isinstance(json_obj, list):
        for item in json_obj:
            result = find_value_for_key(item, target_key)
            if result is not None:
                return result
    return None

def get_value_from_json_file(file_path, key):
    """
    Read a JSON file and return the value for a given key.
    
    :param file_path: Path to the JSON file.
    :param key: The key to search for in the JSON file.
    :return: The value associated with the key or None if the key is not found.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return find_value_for_key(data, key)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except json.JSONDecodeError:
        print("Error decoding JSON")
        return None

file_path = 'demo.json'  
key_to_search = "md5Hex"

value = get_value_from_json_file(file_path, key_to_search)
if value is not None:
    print(f"Value for '{key_to_search}': {value}")
else:
    print(f"Key '{key_to_search}' not found.")
