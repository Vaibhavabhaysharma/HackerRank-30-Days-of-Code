t = int(raw_input())
for _ in range(t):
    line = raw_input()
    first = ""
    second = ""

    for i, c in enumerate(line):
        if (i & 1) == 0:
            first += c
        else:
            second += c
    print first, second
