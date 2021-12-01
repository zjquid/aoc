# advent of code 2021 - day 1

import numpy

print("part 1")
sonar = numpy.loadtxt("input.txt", comments="#")
yes = [];
no = [];

for i in range(2000):
    if (sonar[i] - sonar[i-1]) > 0:
        yes.append(i)
    else:
        no.append(i)

print(len(yes))

#####

print("part 2")

yes2 = []; # initially just added on to the first vector, wasting my time smh
no2 = [];

for i in range(1997):
    if (sonar[i+3] - sonar [i]) > 0:
        yes2.append(i)
    else:
        no2.append(i)

print(len(yes2))
