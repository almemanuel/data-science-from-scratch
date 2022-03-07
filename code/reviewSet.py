primes_below_10 = {2}

primes_below_10.add(3)
primes_below_10.add(5)
primes_below_10.add(7)

print(primes_below_10)
print(len(primes_below_10))
print(2 in primes_below_10)
print(4 in primes_below_10)

stopwords_list = ['a', 'an', 'at'] + ['yet', 'you']
stopwords_set = set(stopwords_list)
print("zip" in stopwords_set)

item_set = {1, 2, 3, 3}
print(item_set)
print(len(item_set))
distinct_item_list = list(item_set)
print(distinct_item_list)