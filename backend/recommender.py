import random
import string


def random_rgb_generator() -> str:
    color = "#" + "".join(random.choices(string.hexdigits, k=6))
    return color.upper()
