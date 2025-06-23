import utility

def get_p_upper(letter: str) -> list[str]:
    return [
        utility.append_space(utility.repeat_4(letter)),
        utility.sandwich_3_spaces(letter),
    ]


def get_p_lower(letter: str) -> list[str]:
    return [
        utility.append_space(utility.repeat_4(letter)),
        utility.append_4_spaces(letter),
        utility.append_4_spaces(letter),
    ]


def get_y_upper(letter: str) -> list[str]:
    return [
        utility.sandwich_3_spaces(letter),
        utility.intersperse_spaces(letter),
    ]


def get_y_lower(letter: str) -> list[str]:
    return [
        utility.sandwich_letter(letter),
        utility.sandwich_letter(letter),
        utility.sandwich_letter(letter),
    ]


def get_o_upper(letter: str) -> list[str]:
    return [
        utility.sandwich_3_letters(letter),
        utility.sandwich_3_spaces(letter),
    ]


def get_o_lower(letter: str) -> list[str]:
    return [
        utility.sandwich_3_spaces(letter),
        utility.sandwich_3_spaces(letter),
        utility.sandwich_3_letters(letter),
    ]


def get_p(letter: str) -> list[str]:
    return get_p_upper(letter) + get_p_lower(letter)


def get_y(letter: str) -> list[str]:
    return get_y_upper(letter) + get_y_lower(letter)


def get_o(letter: str) -> list[str]:
    return get_o_upper(letter) + get_o_lower(letter)
