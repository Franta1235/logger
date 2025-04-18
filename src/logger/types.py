from typing import Any, Literal

KEYS = Literal["function.input", "function.output", "error", "database", "request", None]


class ColorCodes:
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    RESET = "\033[0m"


KEY_COLORS: dict[Any, str] = {
    "function.input": ColorCodes.GREEN,
    "function.output": ColorCodes.YELLOW,
    "error": ColorCodes.RED,
    "database": ColorCodes.CYAN,
    "request": ColorCodes.BLUE,
    None: ColorCodes.WHITE,
}
RESET_COLOR = "\033[0m"
