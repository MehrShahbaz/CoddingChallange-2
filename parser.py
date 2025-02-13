from sys import argv

from helper import remove_extra_space, remove_next_line, parse_json_string, remove_array_brackets

def read_data(file_path: str):
    with open(file_path, "r") as file:
        return file.read().strip()

def check_object_syntax(data:str):
    if not data:
        raise Exception("Invalid Object")
    
    if data[0] != '{' or data[-1] != '}':
        raise Exception("Object Syntax is incorrect")

def check_array_syntax(data:str):
    if not data:
        raise Exception("Invalid Array")
    
    if data[-1] != ']':
        raise Exception("Array Syntax is incorrect", data)

def check_string(data:str) -> bool:
    if not data:
        raise Exception("Invalid String")
    
    data = remove_extra_space(data)
    
    if data[0] != '"' or data[-1] != '"':
        raise Exception("String Syntax is incorrect")
    
    return True

def check_array(data:str) -> bool:
    check_array_syntax(data)
    data = remove_array_brackets(data)
    
    if not data:
        return True
    
    for x in data.split(","):
        check_type(x.strip())
    
    return True

def check_object(data:str) -> bool:
    check_object_syntax(data)
    
    data = remove_next_line(data)
    data = remove_extra_space(data)
    data = parse_json_string(data)
    
    for value in data:
        check_key_value(value)

def check_type(data:str) -> int:
    if data[0] == '"' and check_string(data):
        return
    elif data == 'true' or data == 'false':
        return
    elif data == 'null':
        return
    elif data.isnumeric():
        return
    elif data[0] == '[' and check_array(data):
        return
    elif data[0] == '{':
        return
    else:
        raise Exception("Invalid type", data)

def check_key_value(data:str):
    if len(data) != 3 or ":" not in data[1]:
        raise Exception("Invalid key-value pair", data)

    check_string(data[0])
    check_type(data[2])

def main():
    data = read_data(argv[1])
    check_object(data)
    print("Valid JSON \n", data)

def test(file_path: str) -> str:
    data = read_data(file_path)
    check_object(data)
    return data


if __name__ == "__main__":
    main()