import itertools


def find_max(numbers):
    perms = list(itertools.permutations(numbers))
    return str(max([''.join(map(str, perm)) for perm in perms]))


def find_min(numbers):
    perms = list(itertools.permutations(numbers))
    return str(min([''.join(map(str, perm)) for perm in perms]))


data = [4, 8, 15, 16, 3, 14, 15, 192, 168, 1992, 37, 256, 98, 101, 273, 7787, 918, 39, 1098, 222, 69, 96, 5234, 777]

data = [i ** 2 if i % 2 == 0 else i * 2 for i in data]

data = [i for i in data if i % 24 != 0]

ans_max = []
for i in range(9, 0, -1):
    ans_max.append(find_max([j for j in map(str, data) if j[0] == str(i)]))
ans_max = int("".join(ans_max))

ans_min = []
for i in range(1, 10):
    ans_min.append(find_min([j for j in map(str, data) if j[0] == str(i)]))
ans_min = int("".join(ans_min))

print(ans_min + ans_max)
