from prompt_toolkit import prompt


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt('May I have your name? ')
    print(f"Hello, {name}!")


if __name__ == "__main__":
    welcome_user()
