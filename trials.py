"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    for item in items:
        print(item)

# Should print each item in array
# output_all_items([1, 'hello', True])

def get_all_evens(nums):
    even_nums = []

    for num in nums:
        if num % 2 == 0:
            even_nums.append(num)

    return even_nums

# Should print [8, 10, 2, 2]
assert get_all_evens([7, 8, 10, 1, 2, 2]) == [8, 10, 2, 2]

def get_odd_indices(items):
    result = []

    for i, value in enumerate(items):
        if i % 2 != 0:
            result.append(value)

    return result

# Should print ['hello', 500]
assert get_odd_indices([1, 'hello', True, 500]) == ['hello', 500]

def print_as_numbered_list(items):
    i = 1

    for item in items:
        print(f'{i}. {item}')
        i += 1

# print_as_numbered_list([1, 'hello', True])

def get_range(start, stop):
    nums = []

    for i in range(start, stop):
        nums.append(i)

    return nums

assert get_range(0, 5) == [0, 1, 2, 3, 4]

def censor_vowels(word):
    chars = []

    for letter in word:
        if letter in 'aeiou':
            chars.append('*')
        else:
            chars.append(letter)

    return ''.join(chars)

assert censor_vowels('hello world') == 'h*ll* w*rld'

def snake_to_camel(string):
    camel_case = []

    for word in string.split('_'):
        camel_case.append(f'{word[0].upper()}{word[1:]}')

    return ''.join(camel_case)

assert snake_to_camel('hello_world') == 'HelloWorld'

def longest_word_length(words):
    longest = len(words[0])

    for word in words:
        if longest < len(word):
            longest = len(word)

    return longest

assert longest_word_length(['hello', 'world']) == 5

def truncate(string):
    result = []

    for char in string:
        if len(result) == 0 or char != result[len(result) - 1]:
            result.append(char)

    return ''.join(result)

assert truncate('hi***!!!! wooow') == 'hi*! wow'

def has_balanced_parens(string):
    parens = 0

    for char in string:
        if char == '(':
            parens += 1
        elif char == ')':
            parens -= 1

            if parens < 0:
                return False

    return parens == 0

assert has_balanced_parens('((This) (is) (good))') == True

def compress(string):
    compressed = []

    curr_char = ''
    char_count = 0
    for char in string:
        if char != curr_char:
            compressed.append(curr_char)
        
            if char_count > 1:
                compressed.append(str(char_count))

            curr_char = char
            char_count = 0
    
        char_count += 1

    compressed.append(curr_char)
    if char_count > 1:
        compressed.append(str(char_count))

    return ''.join(compressed)

assert compress('Hello, world! Cows go moooo...') == 'Hel2o, world! Cows go mo4.3'
