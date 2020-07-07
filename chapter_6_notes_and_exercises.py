import numpy as np
a = np.array([230, 10, 284, 39, 76])
cutoff = 200
print(a > cutoff)
a[a > cutoff] = 0
print(a)

# only dimensions of size 1 can stretch when broadcasting
a = np.array([
    [0, 1],
    [2, 3],
    [4, 5],
    ])
b = np.array([10, 100])
print(a * b)

c = np.array([
    [0, 1, 2],
    [3, 4, 5]
])
b = np.array([10, 100])
print(c * b[:, None])
a = np.array([200], dtype='uint8')
a.astype('uint64')

# 1
# d = np.array([200, 25, 60], dtype='uint8')
# while True:
#     d += 10
#     print(d)

# 2
a = np.array([230, 10, 284, 39, 76])
new_value = []
while True:
    a[a <= 100] *= 2
    if ((a > 100).sum () == a.size).astype(np.int):
        new_value = a[(150 < a) & (a < 200)]
        break


print('exercise 2')
print(a)
print(new_value)
