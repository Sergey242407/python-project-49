import random
from brain_games.games import play_game


def generate_question():
    operations = ["+", "-", "*"]
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    operation = random.choice(operations)

    if operation == "+":
        question = f"{num1} + {num2}"
        correct_answer = num1 + num2
    elif operation == "-":
        question = f"{num1} - {num2}"
        correct_answer = num1 - num2
    else:
        question = f"{num1} * {num2}"
        correct_answer = num1 * num2

    return question, correct_answer


def rules():
    return 'What is the result of the expression?'


def main():
    play_game(generate_question, rules)


if __name__ == '__main__':
    main()
