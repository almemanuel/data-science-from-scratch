x = None
assert x is None, "esta é a forma Pythonic de verificar o None"

print(all([True, 1, {3}]))
print(all([True, 1, {}]))
print(any([True, 1, {}]))
print(all([]))
print(any([]))