count = 0
i = 0
while i < 100000:
    cur = 0
    for j in range(i, i + 1000):
        cur += sum([int(j) for j in str(j)])
    print(cur)
    count += cur
    i += 1000
print(count + 1)