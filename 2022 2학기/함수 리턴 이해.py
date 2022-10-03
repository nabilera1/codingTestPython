def reverse(x, y, z):
    return z, y, x


print(reverse(1, 2, 3))
print(reverse('a', 'b', 'c'))
a, b, c = reverse('a', 'b', 'c')

print(c, b, a)
