import random
import brain_games.cli as cli


def ask_question(question):
    print(f"Question: {question}")
    return input("Your answer: ").strip().lower()


def check_answer(user_answer, correct_answer):
    if user_answer == str(correct_answer):
        print("Correct!")
        return True
    else:
        print(f"'{user_answer}' is wrong answer ;(. "
              f"Correct answer was '{correct_answer}'.")
        return False


def play_game(game_logic, rules):
    name = cli.welcome_user()
    rules = rules()
    print(rules)

    rounds = 3
    for _ in range(rounds):
        question, correct_answer = game_logic()
        user_answer = ask_question(question)
        if not check_answer(user_answer, correct_answer):
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")
