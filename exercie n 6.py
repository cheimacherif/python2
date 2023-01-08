#exercie n 6

num_set = set([0, 1, 2, 3, 4])
for n in num_set:
    print(n, end=' ')
num_set.add(8)
for n in num_set:
    print(n, end=' ')
num_set.discard(8)
for n in num_set:
    print(n, end=' ')

