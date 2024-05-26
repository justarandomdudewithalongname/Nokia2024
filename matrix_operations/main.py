import numpy

with open('./input.txt', 'r') as f:
    lines = f.readlines()

matrices = {}
operations = []
current_matrix = None
reading_matrices = True

for line in lines:
    line = line.strip()
    if not line:
        continue

    if reading_matrices:
        if line in "ABCDEFGHIJ":
            current_matrix = line
            matrices[current_matrix] = []
        elif line == "operations":
            reading_matrices = False
            current_matrix = None
        elif current_matrix:
            matrices[current_matrix].append(list(map(int, line.split())))
    else:
        operations.append(line)

for key in matrices:
    matrices[key] = numpy.array(matrices[key])

results = []
for operation in operations:
    operation = operation.replace('*', '@')
    result = eval(operation, {}, matrices)
    results.append(result)


for i, result in enumerate(results):
    if result is not None:
        print(operations[i])
        for row in result:
            print(' '.join(map(str, row)))
        print()

