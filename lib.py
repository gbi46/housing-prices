from colorama import Back, Fore, init

init(autoreset=True)

def main_header(title):
    return Back.BLUE + "   === == = " + title + " = == ===   "

def sub_header(title, length):
    left_fill_block = ''
    right_fill_block = ''

    match length:
        case 1:
            left_fill_block = " === = "
            right_fill_block = " = ==="
        case 2:
            left_fill_block = " === === = "
            right_fill_block = " = === === "

    return Back.GREEN + left_fill_block + title + right_fill_block
