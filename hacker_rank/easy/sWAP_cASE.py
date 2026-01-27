
def swap_case(s):
    res = ""
    for ch in s:
        if 'A' <= ch <= 'Z':
            res += chr(ord(ch) + 32)
        elif 'a' <= ch <= 'z':
            res += chr(ord(ch) - 32)
        else:
            res += ch
    return res
    # or just res.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)