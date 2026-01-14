from colorama import Back, Fore, init

init(autoreset=True)

class HeaderFormatter:
    def __init__(self, length: int = 1):
        self.length = length

    def main_header(self, title: str) -> str:
        return Back.BLUE + f"   === == = {title} = == ===   "

    def sub_header(self, title: str) -> str:
        left_fill, right_fill = self._get_fill_blocks()
        return Back.GREEN + left_fill + title + right_fill

    def _get_fill_blocks(self) -> tuple[str, str]:
        match self.length:
            case 1:
                return " === = ", " = === "
            case 2:
                return " === === = ", " = === === "
            case _:
                return "", ""

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
