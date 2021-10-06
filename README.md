# Find most common pair task

Write a python function that gets a list of customers' baskets, where each basket is represented as a list of strings (each string represents an item name). You should return a tuple ('item A name', 'item B name') consisted of the two items that were bought together in the same basket the most. If there are several tuples as such, return one of them. Assume that item's name is unique and that a single item cannot be purchased more than once in each basket.

## Tradeoffs

There was no option to discuss possible solutions and tradeoffs, so I included two versions:
1. Space efficient
2. Time efficient


### Space efficient

Concise solution with using of itertools and collections modules.
Use sorting to avoid situations with the same items in a different order.
We have k baskets with n items on average.
Time complexity: O( k * (nlogn + n^2) )
Space complexity: O(n choose 2) - number of generated combos

To run and test the solution, execute:

```bash
python space_efficient.py
```

### Time efficient

To reduce time complexity for sorting, weighted graph-like data structure
is used to store combos frequencies.
Time complexity: O( k * (n^2) )
Space complexity: O(n^2) - to store items as vertexes, edges and weights

To run web server, execute:
```bash
python time_efficient.py
```
