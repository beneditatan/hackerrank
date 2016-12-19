def number_needed(a, b):
    num = 0
    for c in "abcdefghijklmnopqrstuvwxyz":
        num += abs(a.count(c) - b.count(c))
    return num
    pass

a = input().strip()
b = input().strip()

print(number_needed(a, b))