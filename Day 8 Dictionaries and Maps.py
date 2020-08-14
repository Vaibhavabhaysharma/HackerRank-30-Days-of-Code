import sys
n = input()
name_numbers = [raw_input().split() for _ in range(n)]
phone_book = {k: v for k,v in name_numbers}
ls = map(lambda x: x.strip(),sys.stdin.readlines())
for name in ls:
    if name in phone_book:
        print('%s=%s' % (name, phone_book[name]))
    else:
        print('Not found')
