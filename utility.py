# issue 1
def repeat_4(letter: str) -> str:
    """
    returns a string that consists of four times `letter`
    example: repeat_4("a") should return "aaaa"
    """
    return 4 * letter


# issue 2
def append_space(word: str) -> str:
    """
    returns `word` with an added space at the end
    example: append_space("abc") should return "abc "
    """
    word = word + ' '
    return word


# issue 3
def sandwich_3_spaces(letter: str) -> str:
    """
    returns three spaces surrounded by `letter`
    example: sandwich_3_spaces("a") should return "a   a"
    """
    return f"{letter}   {letter}"


# issue 4
def append_4_spaces(word: str) -> str:
    """
    returns `word` with four spaces added at the end
    example: append_4_spaces("abc") should return "abc    "
    """
    return ""


# issue 5
def intersperse_spaces(letter: str) -> str:
    """
    returns a space, `letter`, space, `letter, space merged in a string
    example: intersperse_spaces("a") should return " a a "
    """
    return ""


# issue 6
def sandwich_letter(letter: str) -> str:
    """
    returns a string consisting of `letter` with two spaces at the beginning and end
    example: sandwich_letter("a") should return "  a  "
    """
    return "  " + letter + "  "


# issue 7
def sandwich_3_letters(letter: str) -> str:
    """
    returns a string consisting of three times `letter` in between spaces
    example: sandwich_3_letters("a") should return " aaa "
    """
    return ""
