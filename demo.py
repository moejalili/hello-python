messages = [
    'The quick brown fox jumps over the lazy dog.',
    'Now is the time for all good men to come to the aid of their country.',
    'We the People of the United States, in Order to form a more perfect Union, establish Justice, insure domestic Tranquility, provide for the common defence, promote the general Welfare, and secure the Blessings of Liberty to ourselves and our Posterity, do ordain and establish this Constitution for the United States of America.',
    """ Hey, diddle, diddle,
    Hey Diddle Diddle,
    The cat and the fiddle,
    The cow jumped over the moon.
    The little dog laughed,
    To see such sport,
    And the dish ran away with the spoon."""
]

import string

def strip_non_alpha(txt):
    valid = string.ascii_letters + ' '
    return ''.join([l for l in txt if l in valid])

def count_char(l, haystack):
    return sum([l for n in haystack.lower() if n == l.lower()])

cleaned_messages = [strip_non_alpha(message) for message in messages]
t_count = [count_char('t', message) for message in cleaned_messages]
mean_t_count = sum(t_count) / len(t_count)
print(mean_t_count)
