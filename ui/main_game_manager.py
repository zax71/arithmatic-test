import user_input_provider, operations, random 
from storage_providers import storage_instance
from pupil import Pupil


def _ask_question() -> bool:
    """Asks a question, returns bool as to if question was correct"""
    operation: operations.Operations = operations.random_operation()

    n1 = random.randint(-10, 10)
    n2 = random.randint(-10, 10)

    # Stops divide by zero errors
    while n2 == 0:
        n2 = random.randint(-10, 10)

    answer = user_input_provider.input_float(f"{n1} {str(operation)} {n2}: ")

    return round(answer, 2) == round(operation.calculate(n1, n2), 2)

def start_game():
    question_count = user_input_provider.input_int("How many questions do you want? ")
    # TODO: Get pupil to assign score to
    score = 0
    print("Decimal values should be inputted rounded to 2dp or truncated to 3dp")

    for _ in range(0, question_count):
        if _ask_question() is True:
            score = score + 1

    print(f"Score: {score}/{question_count}: {round((score/question_count)*100)}%")
    # TODO: Finish adding score
    storage_instance.add_score()