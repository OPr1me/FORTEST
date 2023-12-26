data = [4, 8, 15, 16, 3, 14, 15, 192, 168, 1992, 37, 256, 98, 101, 273, 7787, 918, 39, 1098, 222, 69, 96, 5234, 777]

data = [i ** 2 if i % 2 == 0 else i * 2 for i in data]

data = [i for i in data if i % 24 != 0]
print(data)