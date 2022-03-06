x = [1, 2, 3]
y = x + [4, 5, 6]
print(x)
print(y)
print('-' * 10)

x, y = [1, 2] # x = 1; y =2
print(x)
print(y)
print('-' * 10)

_, y = [3, 4] # ignore the first
print(x)
print(y)
print('-' * 10)

my_tuple = (1, 2)
other_tuple = 3, 4
print(my_tuple)
print(other_tuple)
print('-' * 10)

# tuple is a great form to use functions to multiple returns
def sum_and_product(x, y): return (x + y), (x * y)

sp = sum_and_product(2, 3)
s, p = sum_and_product(5, 10)
print(sp)
print(s)
print(p)
print('-' * 10)

empty_dic = dict() # not pythonic
empty_dic = {} # pythonic
grades = {
    'Joel': 80,
    'Tim': 95
}
joels_grade = grades['Joel'] # not pythonic
joel_has_grade = 'Joel' in grades # a bit pythonic
kate_has_grade = 'Kate' in grades # a bit pythonic
joels_grade = grades.get('Joel', 0) # pythonic
kates_grade = grades.get('Kate', 0)
no_ones_grade = grades.get('No One')

print(grades)
print(joel_has_grade)
print(kate_has_grade)
print(joels_grade)
print(kates_grade)
print(no_ones_grade)

grades['Kate'] = 100
print(len(grades))
print(grades)

print('-' * 10)

print(grades.keys())
print(grades.values())
print(grades.items())
