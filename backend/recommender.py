import random
import string


def hexValueGenerator() -> str:
    color = "#" + "".join(random.choices(string.hexdigits, k=6))
    return color.upper()
