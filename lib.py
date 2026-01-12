from colorama import Back, Fore, init

init(autoreset=True)

def main_header(title):
    return Back.BLUE + "   === == = " + title + " = == ===   "
