import letters


def merge_lines(p1, y, o, p2, p3):
    return [f"{a}  {b}  {c}  {d}  {e}" for a, b, c, d, e in zip(p1, y, o, p2, p3)]


def build_full_output():
    p1 = letters.get_p("P")
    y = letters.get_y("Y")
    o = letters.get_o("O")
    p2 = letters.get_p("P")
    p3 = letters.get_p("P")
    return merge_lines(p1, y, o, p2, p3)
