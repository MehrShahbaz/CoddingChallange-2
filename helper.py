import re

def remove_next_line(data:str) -> str:
    return data.replace("\n", "")

def remove_extra_space(data:str) -> str:
    return data.replace(" ", "")

def remove_space(data:str) -> str:
    return data.replace(" ", "")

def remove_object_brackets(data:str) -> str:
    return data.replace("{", "").replace("}", "")

def remove_array_brackets(data:str) -> str:
    return data.replace("[", "").replace("]", "")

def parse_json_string(json_str: str) -> list:
    json_str = json_str.strip()
    
    # Ensure correct spacing for splitting
    json_str = json_str.replace("{", " { ").replace("}", " } ").replace("[", " [ ").replace("]", " ] ").replace(":", " : ").replace(",", " , ")

    # Split by whitespace
    tokens = json_str.split()

    result = []
    i = 0

    while i < len(tokens):
        token = tokens[i]

        # Handle key-value pairs
        if re.match(r'"[^"]*"', token):  # Matches keys like "key"
            key = token
            if i + 2 < len(tokens) and tokens[i + 1] == ":":
                value = tokens[i + 2]

                # If value starts an array or object, keep it as a single string
                if value == "[":
                    array_values = []
                    i += 3  # Skip key, colon, and opening bracket
                    while i < len(tokens) and tokens[i] != "]":
                        if tokens[i] != ",":
                            array_values.append(tokens[i] + ',' if tokens[i + 1] != "]" else tokens[i])
                        i += 1
                    result.append([key, ":", f"[{' '.join(array_values)}]"])
                elif value == "{":
                    obj_values = []
                    i += 3  # Skip key, colon, and opening brace
                    while i < len(tokens) and tokens[i] != "}":
                        if tokens[i] != ",":
                            obj_values.append(tokens[i])
                        i += 1
                    result.append([key, ":", f"{{{' '.join(obj_values)}}}"])
                else:
                    result.append([key, ":", value])

        i += 1

    return result