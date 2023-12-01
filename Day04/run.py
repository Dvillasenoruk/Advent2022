

def EnumerateTasks(card):
    markers = card.split('-')
    return range ( int(markers[0]) , int(markers[1])+1)

def Contains(a,b):
    return   set(a).issub/*set(b)

def PartialOverlap (a,b):
    for x in   set(a).intersection(b):
        return True
    return False
        
runningScore = 0

for line in open("input.txt"):
    pair = line.strip().split(',')
    first = EnumerateTasks(pair[0])
    second = EnumerateTasks(pair[1])
    # if Contains(first,second) or Contains(second,first):
    if PartialOverlap(first,second) :
        runningScore = runningScore + 1
        print(first , second, "have overlop")
    else:
        print(first , second, "have NO overlop")
        

print(runningScore)

