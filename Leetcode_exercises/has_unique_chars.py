##has_unique_chars self development
def has_unique_chars(string):
    if sorted(list(set(string)))==sorted(list(string)):
        return True
    return False
##has_unique_chars original
def has_unique_chars(string):
    char_set = set()
    for char in string:
        if char in char_set:
            return False
        char_set.add(char)
    return True