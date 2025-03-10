"""Gives the user a set of arithmetic questions"""

import pathlib
import random

import operations
import user_input_provider
from storage import SQLiteStorage


def ask_question() -> bool:
    """Asks a question, returns bool as to if question was correct"""
    operation: operations.Operations = operations.random_operation()

    n1 = random.randint(-10, 10)
    n2 = random.randint(-10, 10)

    # Stops divide by zero errors
    while n2 == 0:
        n2 = random.randint(-10, 10)

    answer = user_input_provider.input_float(f"{n1} {str(operation)} {n2}: ")

    return round(answer, 2) == round(operation.calculate(n1, n2), 2)


def main():
    """The main function"""
    storage = SQLiteStorage(pathlib.Path(__file__).parent.resolve() / "database.db")

    question_count = user_input_provider.input_int("How many questions do you want? ")
    student_name = input("Enter your name: ")
    score = 0
    print("Decimal values should be inputted rounded to 2dp or truncated to 3dp")

    for _ in range(0, question_count):
        if ask_question() is True:
            score = score + 1

    print(f"Score: {score}/{question_count}: {round((score/question_count)*100)}%")


if __name__ == "__main__":
    main()
