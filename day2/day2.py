# advent of code 2021 - day 2
print("day 2 - both parts")

route = open('input.txt','r',encoding='utf-8')
dirs = route.readlines()

vert = []
vert2 = []
horiz = []
aim = 0

for i in range(len(dirs)):
    current = dirs[i]
    x = int(current[len(current) -2])
    if dirs[i].startswith("f"):
        horiz.append(x)
        vert2.append(aim * x)
    elif dirs[i].startswith("u"):
        vert.append(-x)
        aim = aim - x
    elif dirs[i].startswith("d"):
        vert.append(x)
        aim = aim + x
        
print(sum(horiz) * sum(vert)) # silver
print(sum(horiz) * sum(vert2)) # gold
#####
