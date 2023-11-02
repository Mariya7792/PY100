last = 9
for i in range(2, 10):
    for a in range(2, 10):
        result = i * a
        end = ' ' if a != 9 else ""
        print(f'{result:2}', end=end)
    print()
