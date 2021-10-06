from itertools import combinations
from collections import Counter
from test_cases import run_test_cases

def find_most_common_basket(baskets):
    ITEMS_TOGETHER = 2
    if not baskets:
        return ('','')
    combos = []
    for basket in baskets:
        sorted_basket = sorted(basket)
        combos += [combo for combo in combinations(sorted_basket, ITEMS_TOGETHER)]
    combos_count = Counter(combos)
    return max(combos_count, key=lambda c: combos_count[c]) if combos_count else ('','')


run_test_cases(find_most_common_basket)
