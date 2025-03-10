def input_str(question: str) -> str:
    """Takes an input of a string and ensures that it is not empty"""

    while (in_str := input(question)) == "":
        print("Your answer cannot be empty")
    
    return in_str

def input_float(question: str) -> float:
    while is_float((in_str := input_str(question))) == False:
        print("Must be a float")
    
    return float(in_str)

def input_int(question: str) -> int:
    while is_positive_int(in_str := input_str(question)) == False:
        print("Must be positive int")
    
    return int(in_str)

def is_float(element: any) -> bool:
    #If you expect None to be passed:
    if element is None: 
        return False
        
    try:
        float(element)
        return True
    except ValueError:
        return False

def is_positive_int(element: any) -> bool:
    #If you expect None to be passed:
    if element is None: 
        return False
    try:
        number = int(element)
        if number < 0:
            return False
        return True
    except ValueError:
        return False

        