from difflib import SequenceMatcher
while True:
    try:
        a = input()
        b = input()
    except EOFError:
        break

    subStr = SequenceMatcher(None, a, b)
    c = subStr.find_longest_match(0, len(a), 0, len(b))
    print(c.size)
