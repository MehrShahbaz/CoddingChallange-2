import re
from helper import remove_extra_space, remove_object_brackets, remove_next_line
from constants import FILE_PATHS_STEP_3

def read_data() -> str:
    return open(FILE_PATHS_STEP_3["invalid"], "r").read().strip()

def check_object_syntax(data:str) -> str:
    if not data:
        raise Exception("Empty Object")
    
    if data[0] != '{' or data[-1] != '}':
        raise Exception("Syntax is incorrect")

def check_string(data:str) -> bool:
    if not data:
        raise Exception("Empty String")
    
    data = remove_extra_space(data)
    
    if data[0] != '"' or data[-1] != '"':
        raise Exception("Syntax is incorrect")
    
    return True

def check_type(data:str) -> int:
    if data[0] == '"' and check_string(data):
        print("String", data)
        return
    elif data == 'true' or data == 'false':
        print("Boolean", data)
        return
    elif data == 'null':
        print("Null", data)
        return
    elif data.isnumeric():
        print("Number", data)
        return
    else:
        raise Exception("Invalid type", data)

def check_key_value(data:str):
    res = [s for s in re.split(r'(\s*:\s*)', data) if s.strip()]
    if len(res) != 3 or ":" not in res[1]:
        raise Exception("Invalid key-value pair", data)

    check_string(res[0])
    check_type(res[2])

def main():
    data = orignal_data = read_data()
    check_object_syntax(data)
    
    data = remove_object_brackets(data)
    data = remove_next_line(data)
    data = data.split(",")
    
    for value in data:
        check_key_value(value)
    
    print("Valid JSON \n", orignal_data)



main()