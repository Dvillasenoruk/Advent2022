
def chunkstring(string, length):
    return list(string[0+i:length+i] for i in range(0, len(string), length))
      



SculptLines = []
MoveLines = []

for line in open("input.txt"):
    if line.strip().startswith('['):
        SculptLines.append(line)
        
    if line.startswith('move'):
        MoveLines.append(line)
        
containerstacks = None
        
for line in SculptLines:
    parts = chunkstring(line, 4)
    if containerstacks == None :
        containerstacks = []
        for i in parts:
            containerstacks.append([])

    print (parts)
    
    for i in range (0, len(parts)):
        if parts[i].startswith('['):        
           containerstacks[i].append(parts[i].strip())
  
for stack in containerstacks:
    stack.reverse()          
            
for stack in containerstacks:
    print (stack)

for move in MoveLines:
#    print (move)
    parts = move.strip().split (' ')
    rep = int(parts[1])
    start = int (parts[3]) -1
    end =int (parts[5]) -1
    
    #for i in range(0, rep):
    #    containerstacks[end].append(containerstacks[start].pop())

    print("before start")
    print(containerstacks[start])

    print("before end" )
    print(containerstacks[end])
    containerstacks[end].append(containerstacks[start][:-1*rep])
        
    
    print("after start")
    print(containerstacks[start])

    print("after end" )
    print(containerstacks[end])
    
#    for stack in containerstacks:
#        print (stack)
        
        
for stack in containerstacks:
     print (stack[-1][1])