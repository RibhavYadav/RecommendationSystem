import random
from typing import List, Tuple


class Recommender:
    def __init__(self):
        self.chosen_colours: List[Tuple[int, int, int]] = []

    def get_colour(self) -> str:
        if len(self.chosen_colours) < 3:
            return self.get_random_colour()
        else:
            return self.generate_similar_colours()

    def get_random_colour(self) -> str:
        colour = tuple(random.randint(0, 255) for _ in range(3))
        return self.rgb_to_hex(colour)

    def generate_similar_colours(self) -> str:
        centroid = tuple(sum(c[i] for c in self.chosen_colours) // len(self.chosen_colours) for i in range(3))
        noise = tuple(random.randint(-48, 48) for _ in range(3))
        new_colour = tuple(min(max(centroid[i] + noise[i], 0), 255) for i in range(3))
        return self.rgb_to_hex(new_colour)

    def rgb_to_hex(self, rgb: Tuple[int, int, int]) -> str:
        return "#{:02x}{:02x}{:02x}".format(*rgb)

    def hex_to_rgb(self, hex_value: str) -> Tuple[int, int, int]:
        hex_value = hex_value.lstrip('#')
        return tuple(int(hex_value[i:i + 2], 16) for i in (0, 2, 4))
