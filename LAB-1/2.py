def longestSubstring(s):
    a = []                                                              # for current value
    b = []                                                              #Used to store all substrings

    #Finding all possible substrings without repeating characters
    for c in s:
        if c in a:
            b.append(''.join(a))
            d = a.index(c) + 1
            a = a[d:]
        a += c
    b.append(''.join(a))
    print("substrings without repeating characters : ", b)

    #Finding and displaying the substrings with max length
    length = max(len(x) for x in b)
    for x in b:
        if len(x) == length:
            print(x,len(x))

str = input("Enter substring : ")
longestSubstring(str)
pwwkew
