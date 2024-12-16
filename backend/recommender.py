import random
import string
import itertools
import math


class Recommender:
    def __init__(self):
        self.chosen_colours: list[list[int]] = []

    def get_colour(self) -> str:
        if len(self.chosen_colours) < 3:
            return self.get_random_colour()
        else:
            return random.choice(self.generate_similar_colours())

    def get_random_colour(self) -> str:
        color = "#" + "".join(random.choices(string.hexdigits, k=6))
        return color.upper()

    def intensity_difference(self, intensity1: int, intensity2: int, method: str = "euclidean") -> int:
        if method == "mean":
            return ((intensity1 + intensity2) // 2) % 256
        if method == "abs":
            return abs(intensity1 - intensity2)
        if method == "max":
            return max(intensity1, intensity2)
        if method == "euclidean":
            return int(math.sqrt(math.pow(intensity1, 2) + math.pow(intensity2, 2))) % 256

    def generate_similar_colours(self) -> list[str]:
        pairwise_combinations = itertools.combinations(self.chosen_colours, 2)
        new_colours: list[str] = []
        for colour1, colour2 in pairwise_combinations:
            new_intensity = [0, 0, 0]
            for idx, intensity in enumerate(zip(colour1, colour2)):
                new_intensity[idx] = str(hex(self.intensity_difference(intensity[0], intensity[1])))[2:].zfill(2)
            new_colour = "#" + "".join(new_intensity)
            new_colours.append(new_colour)
        return new_colours
