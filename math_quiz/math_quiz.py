import random


def generateRandomInt(min, max):
    """
    Generates a random integer within the specified range.

    Args:
        min (int): The minimum value.
        max (int): The maximum value.

    Returns:
        int: A random integer between min and max.
    """
    return random.randint(min, max)


def generateRandomOperator():
    """
    Generates a random operator from the list.

    Args: None

    Returns:
        str: A random string with the generated math operator.
    """
    return random.choice(['+', '-', '*'])


def buildMathProblem(n1, n2, operator):
    """
    Builds a math problem given two integers and math operator.

    Args:
        n1 (int): First integer.
        n2 (int): Second integer.
        operator (str): Math operator.

    Returns:
        tuple: A string with the problem and an incorrect answer.
    """

    p = f"{n1} {operator} {n2}"

    # Fixed bug: Calculate the correct answer based on the math operator
    if operator == '+': a = n1 + n2
    elif operator == '-': a = n1 - n2
    else: a = n1 * n2
    return p, a

def mathQuiz():
    """
    Runs the math quiz game and gives the user randomly generated math problems.
    """
    score = 0
    # Defines the number of problems the user will receive
    # Fixed bug: Changed number of problems generated from 3.14159265359 to 3. We need an integer to run the game loop
    problemsCount = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(problemsCount):
        # Generates two integers and the math operator
        # Fixed bug: random.randint only works with integers, so we have to update the upperbound 5.5 to 5
        n1 = generateRandomInt(1, 10); n2 = generateRandomInt(1, 5); operator = generateRandomOperator()

        PROBLEM, ANSWER = buildMathProblem(n1, n2, operator)
        print(f"\nQuestion: {PROBLEM}")
        #userAnswer = input("Your answer: ")
        #userAnswer = int(userAnswer)

        # Error handling: Ensure user input is a valid integer
        while True:  # Loop until a valid answer is given
            try:
                userAnswer = int(input("Your answer: "))
                break  # Exit loop if input is valid
            except ValueError:
                print("Invalid input. Please enter an integer.")

        if userAnswer == ANSWER:
            print("Correct! You earned a point.")
            score += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {score}/{problemsCount}")

if __name__ == "__main__":
    mathQuiz()
