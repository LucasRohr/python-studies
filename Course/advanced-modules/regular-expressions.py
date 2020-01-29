import re

print(re.search('e', 'texto'))

patterns = ['a', 'b']

text = 'aeioua'

for pat in patterns:

    if (re.search(pat, text)):
        print('\n')
        print(text)
        print(f'pattern {pat} found\n')
    else:
        print(text)
        print(f'pattern {pat} not found\n')

print(re.split(patterns[0], text))
print(re.findall('a', text))

print('')

# -----------------------

def multi_re_find(patterns,phrase):
    '''
    Takes in a list of regex patterns
    Prints a list of all matches
    '''
    for pattern in patterns:
        print('Searching the phrase using the re check: %r' %(pattern))
        print(re.findall(pattern,phrase))
        print('\n')

test_patterns=[ r'\d+', # sequence of digits
                r'\D+', # sequence of non-digits
                r'\s+', # sequence of whitespace
                r'\S+', # sequence of non-whitespace
                r'\w+', # alphanumeric characters
                r'\W+', # non-alphanumeric
                ]

test_patterns = [ 'sd*',     # s followed by zero or more d's
                'sd+',          # s followed by one or more d's
                'sd?',          # s followed by zero or one d's
                'sd{3}',        # s followed by three d's
                'sd{2,3}',      # s followed by two to three d's
                ]

text = 'Some thing to Test regex # 123 sdd sddd'

multi_re_find(test_patterns, text)