plantA = 80000
cresciA = 1.03
plantB = 200000
cresciB = 1.015
anos = 0

while plantA <= plantB:
    plantA = plantA * cresciA
    plantB = plantB * cresciB
    anos += 1

print(anos)