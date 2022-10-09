def simple_translate(tone, chord):
    def generate_map(tone):
        mapping = {}
        for idx, (l, u, d) in enumerate(zip(
            ["i", "ii", "iii", "iv", "v", "vi", "vii"],
            ["I", "II", "III", "IV", "V", "VI", "VII"],
            ["1", "2", "3", "4", "5", "6", "7"],
        )):
            mapping[l] = mapping[u] = mapping[d] = chr(
                (ord(tone) - ord('A') + idx) % 7 + ord('A')
            )
        mapping[""] = ""
        return mapping
    mapping = generate_map(tone[0])
    slash_split = chord.split("/")
    for idx, part in enumerate(slash_split):
        if part[0] in "1234567":
            slash_split[idx] = mapping[part[0]] + part[1:]
        else:
            for pre, c in enumerate(part + " "):
                if c not in "ivIV":
                    break
            slash_split[idx] = mapping[part[:pre]] + part[pre:]
    return "/".join(slash_split)
