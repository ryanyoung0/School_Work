grades=["A", "B", "C", "D", "F"]
cutoffs=[90, 80, 70, 65, 0]

def assigngrade(score, grades=["A", "B", "C", "D", "F"] , cutoffs=[90, 80, 70, 65, 0]):
    for x in range(len(cutoffs)):
        if score >= cutoffs[x]:
            return grades[x]
assigngrade(80, grades, cutoffs)
def droplowest(L):
    L.remove(min(L))

droplowest([1,2,3,5,4])

def average(L):
    sum = 0
    for x in L:
        sum = x + sum
        average2 = sum / len(L)
    return average2
average([1,2,3])
