def remove_next_line(data:str) -> str:
    return data.replace("\n", "")

def remove_extra_space(data:str) -> str:
    return data.replace(" ", "")

def remove_space(data:str) -> str:
    return data.replace(" ", "")

def remove_object_brackets(data:str) -> str:
    return data.replace("{", "").replace("}", "")
