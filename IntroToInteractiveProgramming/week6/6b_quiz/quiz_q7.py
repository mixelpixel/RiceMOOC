n = 100
numbers = range(2, n)
results = []
while len(numbers) > 0:
    results.append(numbers[0])
    new = [i for i in numbers if i % results[-1] == 0]
    print new
    [numbers.remove(i) for i in new]
print len(results), results
