from os import system, name

def clear_console() -> None:

    # for Windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux
    else:
        _ = system('clear')
    

def get_numeric(prompt: str) -> int:
    while True:
        try:
            choice = int(input(prompt))
            break
        except ValueError:
            print("You must enter a number")
    return choice

def wait_before_proceeding() -> None:
    _ = input("Press <Enter> to proceed...")

def choice_menu(choices: dict[int:str]) -> int:
    for number, action in choices.items():
            if hasattr(action, '__call__'):
                print(f"{number}. {action.__name__}")
            else:
                print(f"{number}. {action}")
    choice = get_numeric("Your choice: ")
    while choice not in choices.keys():
        print("Wrong input, choose proper number")
        choice = get_numeric("Your choice: ")
        
    return choice