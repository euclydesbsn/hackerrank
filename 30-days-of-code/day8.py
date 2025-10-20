phoneBook = {}

n = int(input())

for _ in range(n):
    i = input().split()
    phoneBook[i[0]] = i[1]

try:
    while True:
        q = input()
        if q in phoneBook:
            print(f"{q}={phoneBook[q]}")
        else:
            print("Not found")
except EOFError:
    pass