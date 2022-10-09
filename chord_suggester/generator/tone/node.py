import random


class ChordNode:

    def __init__(self, root, qualities, nid):
        self.root = root
        self.qualities = qualities
        self.nid = nid

    @staticmethod
    def chord_to_string(root: str, quality: str):
        if "{}" in root:
            return root.format(quality)
        return root + quality
    
    def random_select(self):
        return self.chord_to_string(self.root, random.choice(self.qualities))
