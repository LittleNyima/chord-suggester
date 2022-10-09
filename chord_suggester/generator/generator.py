import random


class BaseGenerator:
    def __init__(self):
        pass

    def init_phrase(self):
        raise NotImplementedError

    def has_next(self):
        raise NotImplementedError
    
    def next(self):
        raise NotImplementedError
    
    def next_phrase(self):
        raise NotImplementedError


class RandomGenerator(BaseGenerator):
    def __init__(self, tone):
        self.tone = tone
        self.tone_cur_node = -1
    
    def init_phrase(self):
        self.tone_cur_node = random.randint(0, len(self.tone.nodes) - 1)
    
    def has_next(self):
        return self.tone_cur_node in self.tone.edges
    
    def next(self):
        assert self.has_next(), "Generation process is terminated."
        nxt = self.tone.nodes[self.tone_cur_node].random_select()
        self.tone_cur_node = random.choice(self.tone.edges[self.tone_cur_node])
        return nxt

    def next_phrase(self):
        phrase = []
        while self.has_next():
            phrase.append(self.next())
        return phrase