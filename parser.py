def check_object_syntax(data:str):
    if not data:
        raise Exception("Empty Object")
    
    if data[0] != '{' or data[-1] != '}':
        raise Exception("Syntax is incorrect")

def main():
    data = open("./tests/step1/valid.json", "r").read()
    check_object_syntax(data)



main()