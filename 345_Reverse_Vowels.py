def reverseVowels(s):
    """
    :type s: str
    :rtype: str
    """
    vowels = ["a", "o", "e", "i", "u", "A", "O", "E", "I", "U"]
    i = 0
    j = len(s)
    l = list(s)//字符串转成列表
    while  i < j-1:
        if l[i] in vowels and l[j - 1] in vowels:
            l[i], l[j - 1] = l[j - 1], l[i]
            i += 1
            j -= 1
        if l[i] not in vowels:
            i += 1
        if l[j-1] not in vowels:
            j -= 1
    return "".join(l)