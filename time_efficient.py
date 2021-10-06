from test_cases import run_test_cases

def generate_combinations(basket):
    i = 0
    while i < len(basket) - 1:
        j = i + 1
        while j < len(basket):
            yield (basket[i], basket[j])
            j += 1
        i += 1

def add_combo_frequency(frequencies, combo):
    item1, item2 = combo
    if item1 not in frequencies:
        frequencies[item1] = {}
    if item2 not in frequencies[item1]:
        frequencies[item1][item2] = 0
    frequencies[item1][item2] += 1

def find_max_frequent_combo(frequencies):
    max_frequency = (0, ('',''))
    visited = set()
    for item1 in frequencies:
        visited.add(item1)
        for item2 in frequencies[item1]:
            frequency = frequencies[item1][item2]
            if item2 not in visited and item2 in frequencies:
                frequency += frequencies[item2].get(item1,0)
            if frequency > max_frequency[0]:
                max_frequency = (frequency, (item1, item2))
    return max_frequency[1]

def find_most_common_basket(baskets):
    if not baskets:
        return ('','')

    combo_frequencies = {}

    for basket in baskets:
        for combo in generate_combinations(basket):
            add_combo_frequency(combo_frequencies, combo)

    return find_max_frequent_combo(combo_frequencies)

run_test_cases(find_most_common_basket)
