def run_test_cases(testing_func):
    #test case 1
    inp = []
    output = ('', '')
    result = testing_func(inp)
    print('test case 1:')
    print('expected: ', output, 'result: ', result)

    #test case 2
    inp = [['banana']]
    output = ('', '')
    result = testing_func(inp)
    print('test case 2:')
    print('expected: ', output, 'result: ', result)

    #test case 3
    inp = [
        ['ice', 'pie', 'coke', 'apple'],
        ['ice', 'solt', 'apple', 'juce']
        ]
    output = ('apple', 'ice')
    result = testing_func(inp)
    print('test case 3:')
    print('expected: ', output, 'result: ', result)

    #test case 4
    inp = [
        ['ice', 'pie', 'coke', 'apple'],
        ['apple', 'solt', 'ice', 'juce']
        ]
    output = ('apple', 'ice')
    result = testing_func(inp)
    print('test case 4:')
    print('expected: ', output, 'result: ', result)

    #test case 5
    inp =  [
        ['coke', 'ice', 'meat', 'ketchup', 'apple', 'banana'],
        ['coke', 'bread', 'meat', 'ketchup', 'apple', 'strawberry'],
        ['coke', 'pepsi', 'meat', 'ketchup', 'apple', 'banana'],
        ['pepsi', 'ice', 'meat', 'bread', 'tomato', 'cucumber'],
        ['sprite', 'rum', 'meat', 'ketchup', 'strawberry', 'banana'],
        ]
    output = ('ketchup', 'meat')
    result = testing_func(inp)
    print('test case 5:')
    print('expected: ', output, 'result: ', result)
