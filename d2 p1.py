def is_perfect_square(n):
    a = n // 2
    b = set([a])
    while a * a != n:
        a = (a + (n // a)) // 2
        if a in b: return False
        b.add(a)
    return True

print(is_perfect_square(5))
