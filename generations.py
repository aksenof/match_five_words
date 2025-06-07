import random
from typing import Any


def generate_rounds() -> list[dict[str, Any]]:
    with open("words/russian_nouns_top50.txt", encoding="utf-8") as f:
        all_nouns = f.read().splitlines()

    with open("words/russian_adjectives_top50.txt", encoding="utf-8") as f:
        all_adjectives = f.read().splitlines()

    random.shuffle(all_nouns)
    random.shuffle(all_adjectives)

    group_word_count = 5
    len_words = len(all_nouns)
    group_count = int(len_words / group_word_count)

    rounds = []
    for i in range(group_count):
        nouns_group = all_nouns[i*5:(i+1)*5]
        adjectives_group = all_adjectives[i*5:(i+1)*5]
        rounds.append({
            "round_number": i + 1,
            "nouns": nouns_group,
            "adjectives": adjectives_group
        })

    return rounds
