# advent of code - day 3
print("part 1")
diagnostic = open('input.txt', 'r')
lines = diagnostic.readlines()

matrix2 = [[0 for x in range(1000)] for y in range(12)]
matrix = [[0 for x in range(12)] for y in range(1000)]
# converts to matrix
for i in range(12):
    for j in range(1000):
        current = lines[j]
        matrix[j][i] =int(current[i])

# makes another matrix for part 2... did part 1 the wrong way lol
for i in range(12):
    for j in range(1000):
        current = lines[j]
        matrix2[i][j] =int(current[i])


sums = [sum(x) for x in zip(*matrix)]

gamma = []
epsilon = []

for i in range(12):
    if sums[i] > 500:
        gamma.append(1)
        epsilon.append(0)
    else:
        gamma.append(0)
        epsilon.append(1)

gamma_num = int(''.join(str(e) for e in gamma),2)
epsilon_num = int(''.join(str(e) for e in epsilon),2)

print(gamma_num * epsilon_num)
#####
print("part 2") # using matrix 2

#for i in range(12):
#    print(matrix2[i][0])

winning_nums = []
losing_nums = []

# reuse sums for the first bit
if sums[0] > 500:
    winning_nums.append(1)
    losing_nums.append(0)
else:
    winning_nums.append(0)
    losing_nums.append(1)

o_keep = [] # o2 - winners
c_keep = [] # co2 - losers

winrar = winning_nums[0]

for i in range(1000):
    current = matrix2[0]
    if current[i] == winrar:
        o_keep.append(matrix[i])
    else:
        c_keep.append(matrix[i])

o2 = [[0 for x in range(12)] for y in range(len(o_keep))]
co2 = [[0 for x in range(12)] for y in range(len(c_keep))]
        
# convert to matrix - o2 
for i in range(12):
    for j in range(len(o_keep)):
        current = o_keep[j]
        o2[j][i] =int(current[i])
        
# convert to matrix - co2
for i in range(12):
    for j in range(len(c_keep)):
        current = c_keep[j]
        co2[j][i] =int(current[i])

o_iter2_check = [sum(x) for x in zip(*o2)]
c_iter2_check = [sum(x) for x in zip(*co2)]

if o_iter2_check[0] > 500:
    # don't care about losing nums in o2 anymore
    winning_nums.append(1)
else:
    winning_nums.append(0)

if c_iter2_check[0] > 500:
    # don't care about winning nums in co2 anymore
    losing_nums.append(1)
else:
    losing_nums.append(0)

winrar = winning_nums[1] # 2nd bit
loserar = losing_nums[1]
o_3 = []
c_3 = []

for i in range(len(o_keep)):
    current = o2[0]
    if current[i] == winrar:
        # don't care about co2 matrix
        o_3.append(matrix[i])
        
for i in range(len(c_keep)):
    current = co2[0]
    if current[i] == loserar:
        # don't care about co2 matrix
        c_3.append(matrix[i])
