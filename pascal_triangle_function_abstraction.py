from math import pi as PI

# 1
_1 = 3
print(f'{_1 = }')

# 1 2 1
_2 = lambda _1: _1 * 2
print(f'{_2(_1) = }')

# 1 4 6 4 1
_6 = lambda _4: lambda _1: [_4(x) for x in _1]
_4 = _2
_1 = [1,2,3]
print(f'{_6(_4)(_1) = }')

# 1 6 15 20 15 6 1
_20 = lambda _15: lambda _6: lambda _1: sum(_15(_6)(_1)) / len(_1)
_15 = _6
_6 = _2
_1 = [1,2,3]
print(f'{_20(_15)(_6)(_1) = }')


# Example: Pythagorean Theorem
_20 = lambda _15: lambda _6: lambda _1: sum(_15(_6)(_1)) ** .5
_15 = lambda f: lambda xs: map(f, xs)
_6 = lambda x: x ** 2
_1 = [5, 12]
print(f'Pythagorean Theorem: {_1} = {_20(_15)(_6)(_1)}') # 13.0


# Example: Euclidean Distance
_20 = lambda _15: lambda _6: lambda _1: sum(_15(_6)(_1)) ** .5
_15 = lambda f: lambda xys: [f(x,y) for x,y in zip(xys[0], xys[1])]
_6 = lambda x,y: (x - y) ** 2
_1 = ([0,0], [1,1]) 
print(f'Euclidean Distance: {_1}: {_20(_15)(_6)(_1)}') # sqrt(2)


# Example: LN Norm (N > 0)
_20 = lambda _15: lambda _6: lambda _1, n: sum(map(lambda x: abs(x)**n, _15(_6)(_1))) ** (1/n)
_15 = lambda f: lambda xys: [f(x,y) for x,y in zip(xys[0], xys[1])]
_6 = lambda x,y: (x - y)
_1 = ([0,1,0], [1,0,0])
print(f'L1 Norm: {_1}: {_20(_15)(_6)(_1, 1)}') # 2
print(f'L2 Norm: {_1}: {_20(_15)(_6)(_1, 2)}') # sqrt(2)
print(f'L3 Norm: {_1}: {_20(_15)(_6)(_1, 3)}')
print(f'Lπ Norm: {_1}: {_20(_15)(_6)(_1, PI)}')


# Refactored Example: LN Norm (N > 0)
transpose = lambda arr2d: zip(*arr2d)
apply = lambda f: lambda xys: [f(x,y) for x,y in xys]
diff = lambda x,y: (x - y)
ln_norm = lambda vs, n: sum(abs(x)**n for x in apply(diff)(transpose(vs))) ** (1/n)
vectors = [[0,1,0], [1,0,0]]

print(f'Refactored L1 Norm: {vectors}: {ln_norm(vectors, 1)}') # 2
print(f'Refactored L2 Norm: {vectors}: {ln_norm(vectors, 2)}') # sqrt(2)
print(f'Refactored L3 Norm: {vectors}: {ln_norm(vectors, 3)}')
print(f'Refactored Lπ Norm: {vectors}: {ln_norm(vectors, PI)}')








