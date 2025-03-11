"""Utility methods to help with taking user input"""


def input_str(question: str) -> str:
    """Takes an input of a string and ensures that it is not empty"""

    while not (in_str := input(question)).strip():
        print("Your answer cannot be empty")

    return in_str


def input_float(question: str) -> float:
    """Takes an input and checks that it is a valid float"""
    while is_float((in_str := input_str(question))) is False:
        print("Must be a float")

    return float(in_str)


def input_int(question: str) -> int:
    """Checks if an input is an int and returns the input"""
    while is_positive_int(in_str := input_str(question)) is False:
        print("Must be positive int")

    return int(in_str)


def ask_menu(title: str, questions: list[str]) -> int:
    """Asks the user in the form of a menu"""
    print(title)
    for i, question in enumerate(questions):
        print(f"{i+1}. {question}")
    
    while (in_int := input_int("> ")) > len(questions):
        print("Your answer is out of range")
    
    return in_int

def is_float(element: str) -> bool:
    """Checks if the entered element is a float"""
    try:
        float(element)
        return True
    except ValueError:
        return False


def is_positive_int(element: str) -> bool:
    """Checks if the entered element is a positive int"""
    try:
        number = int(element)
        if number <= 0:
            return False
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    print(ask_menu("Title", ["First Q", "Second Q"]))
    

