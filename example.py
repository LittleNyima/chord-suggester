from chord_suggester.generator import RandomGenerator, StephenMugglin
from chord_suggester.util import simple_translate

generator = RandomGenerator(StephenMugglin())
generator.init_phrase()
phrase = generator.next_phrase()
tone = "C"
print(phrase)
print(list(map(lambda chord: simple_translate(tone, chord), phrase)))
