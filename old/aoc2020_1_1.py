import numpy
print("advent 1 - testing in python")
#####

inpu = numpy.loadtxt("input.txt", comments="#")

#inpu = [1721,979,366,299,675,1456]; # input values
outpu = []; # initialize output vector

for i in inpu:
    for j in inpu:
        if (2020-i) == j:
            # checks each index
            outpu.append(i); # adds successful values (not indices) to output vector
            break
print(int(outpu[0]*outpu[1]))
