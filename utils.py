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
