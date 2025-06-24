import utility


# issue 8
def get_p_upper(letter: str) -> list[str]:
    """
    returns a list containing the results of 
    `utility.append_space(utility.repeat_4(letter))` and `utility.sandwich_3_spaces(letter)`
    """
    return []


# issue 9
def get_p_lower(letter: str) -> list[str]:
    """
    returns a list containing the results of `utility.append_space(utility.repeat_4(letter))`
    and two times the result of `utility.append_4_spaces(letter),`
    """
    return []


# issue 10
def get_y_upper(letter: str) -> list[str]:
    """
    returns a list containing the results of `utility.sandwich_3_spaces(letter)`
    and `utility.intersperse_spaces(letter)`
    """
    return []


# issue 11
def get_y_lower(letter: str) -> list[str]:
    """
    returns a list containing the result of `utility.sandwich_letter(letter)`
    three times
    """
    return [utility.sandwich_letter(letter)]*3


# issue 12
def get_o_upper(letter: str) -> list[str]:
    """
    returns a list containing the results of `utility.sandwich_3_letters(letter)`
    and `utility.sandwich_3_spaces(letter)`
    """
    return []


# issue 13
def get_o_lower(letter: str) -> list[str]:
    """
    returns a list containing the result of `utility.sandwich_3_spaces(letter)` two
    times and the result of `utility.sandwich_3_letters(letter)`
    """
    return []


# issue 14
def get_p(letter: str) -> list[str]:
    """
    returns the sum of get_p_upper(letter) and get_p_lower(letter)
    """
    return []


# issue 15
def get_y(letter: str) -> list[str]:
    """
    returns the sum of get_y_upper(letter) and get_y_lower(letter)
    """
    return get_y_upper(letter) + get_y_lower(letter)


# issue 16
def get_o(letter: str) -> list[str]:
    """
    returns the sum of get_o_upper(letter) and get_o_lower(letter)
    """
    return []
