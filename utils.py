def get_numeric(prompt: str) -> int:
    while True:
        try:
            choice = int(input(prompt))
            break
        except ValueError:
            print("You must enter a number")
    return choice
