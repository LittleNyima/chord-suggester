from chord_suggester.generator.tone import ChordNode


class BaseRule:

    def __init__(self):
        pass


class StephenMugglin(BaseRule):
    """ Rule for chord generation according to Stephen Mugglin chord maps.
        Please refer to https://mugglinworks.com/chordmaps/GenericMap.pdf
        for more information.
    """

    def __init__(self):
        self.nodes = [
            ChordNode("III",    ["m7b5"],                          0),
            ChordNode("VI",     ["", "7", "9", "b9"],              1),
            ChordNode("I#",     ["dim7"],                          2),
            ChordNode("ii",     ["m", "m7", "m9"],                 3),
            ChordNode("V",      ["", "7", "9", "11", "13", "sus"], 4),
            ChordNode("IV#",    ["m7b5"],                          5),
            ChordNode("II",     ["", "7", "9", "b9"],              6),
            ChordNode("VI",     ["m7b5", "b3"],                    7),
            ChordNode("IV#",    ["m7b5"],                          8),
            ChordNode("VII",    ["", "7", "9", "b9"],              9),
            ChordNode("II#",    ["dim7"],                          10),
            ChordNode("iii",    ["m", "m7"],                       11),
            ChordNode("vi",     ["m", "m7", "m9"],                 12),
            ChordNode("V#",     ["dim7"],                          13),
            ChordNode("III",    ["", "7", "9", "b9"],              14),
            ChordNode("VI",     ["m7b5"],                          15),
            ChordNode("V",      ["m", "7"],                        16),
            ChordNode("I",      ["", "7", "9", "b9"],              17),
            ChordNode("III",    ["m7b5"],                          18),
            ChordNode("IV",     ["", "6", "M7", "m", "m6"],        19),
            ChordNode("I/3",    [""],                              20),
            ChordNode("ii",     ["m", "m7", "m9"],                 21),
            ChordNode("I#",     ["dim7"],                          22),
            ChordNode("VI",     ["", "7", "9", "b9"],              23),
            ChordNode("III",    ["m7b5"],                          24),
            ChordNode("I{}/3b", ["dim"],                           25),
            ChordNode("I",      ["m6"],                            26),
            ChordNode("II",     ["", "7", "9", "b9"],              27),
            ChordNode("V/2",    [""],                              28),
            ChordNode("IV#",    ["m7b5"],                          29),
            ChordNode("V",      ["", "7", "9", "11", "13", "sus"], 30),
            ChordNode("IV",     ["m7"],                            31),
            ChordNode("IIb",    ["7"],                             32),
            ChordNode("I/5",    [""],                              33),
            ChordNode("VIb",    ["7"],                             34),
            ChordNode("IV#",    ["m7b5"],                          35),
            ChordNode("VIIb",   ["9"],                             36),
            ChordNode("VIb",    [""],                              37),
            ChordNode("VIIb",   ["", "9"],                         38),
            ChordNode("IV/1",   [""],                              39),
            ChordNode("V/1",    [""],                              40),
            ChordNode("I",      ["", "2", "6", "M7", "M9", "sus"], 41),
        ]
        self.edges = {
            0: [1],
            1: [3],
            2: [3],
            3: [4, 11],
            4: [11, 12],
            5: [4],
            6: [4],
            7: [6],
            8: [9],
            9: [11],
            10: [11],
            11: [12, 19],
            12: [19, 21],
            13: [12],
            14: [12],
            15: [14],
            16: [17],
            17: [19],
            18: [19],
            19: [20, 21, 30],
            20: [21],
            21: [30, 33],
            22: [21],
            23: [21],
            24: [23],
            25: [21],
            26: [27, 28],
            27: [30],
            28: [27],
            29: [30],
            30: [41],
            31: [41],
            32: [41],
            33: [30],
            34: [33],
            35: [33],
            36: [33],
            37: [38],
            38: [41],
            39: [41],
            40: [41],
            41: [-1, 39, 40],
        }
