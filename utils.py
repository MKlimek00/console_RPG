from os import system, name


def clear_console() -> None:
    """
    Funkcja czyszcząca konsolę
    """

    # for Windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux
    else:
        _ = system('clear')


def get_numeric(prompt: str) -> int:
    """
    Funkcja bezpiecznego pobrania liczby całkowitej od gracza.
    """
    while True:
        try:
            choice = int(input(prompt))
            break
        except ValueError:
            print("You must enter a number")
    return choice


def wait_before_proceeding() -> None:
    """
    Funkcja oczekiwania na reakcje gracza, żeby zdążył wszystko przeczytać zanim pójdzie dalej.
    """
    _ = input("Press <Enter> to proceed...")


def choice_menu(choices: dict[int:str]) -> int:
    """
    Funkcja zapewniająca poprawny wybór jednej z kilku opcji prezentowanej dla gracza.
    """
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


def normalize_probabilities(probabilities: list[float]) -> list[float]:
    """
    Funkcja normalizująca listę liczb tak, aby suma liczb w liście wynosiła 1
    """
    return [prob/sum(probabilities) for prob in probabilities]
