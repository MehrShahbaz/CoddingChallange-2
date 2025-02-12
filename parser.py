import re

FILE_PATHS_STEP_2 = {
    "valid": "./tests/step2/valid.json",
    "valid2": "./tests/step2/valid2.json",
    "invalid": "./tests/step2/invalid.json",
    "invalid2": "./tests/step2/invalid2.json",
}

def read_data() -> str:
    return open(FILE_PATHS_STEP_2["valid2"], "r").read().strip()

def remove_next_line(data:str) -> str:
    return data.replace("\n", "")

def remove_extra_space(data:str) -> str:
    return data.replace(" ", "")

def remove_space(data:str) -> str:
    return data.replace(" ", "")

def remove_object_brackets(data:str) -> str:
    return data.replace("{", "").replace("}", "")

def check_object_syntax(data:str) -> str:
    if not data:
        raise Exception("Empty Object")
    
    if data[0] != '{' or data[-1] != '}':
        raise Exception("Syntax is incorrect")

def check_string(data:str):
    if not data:
        raise Exception("Empty String")
    
    data = remove_extra_space(data)
    
    if data[0] != '"' or data[-1] != '"':
        raise Exception("Syntax is incorrect")

def check_key_value(data:str):
    res = [s for s in re.split(r'(\s*:\s*)', data) if s.strip()]
    if len(res) != 3 or ":" not in res[1]:
        raise Exception("Invalid key-value pair", data)

    check_string(res[0])
    check_string(res[2])

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