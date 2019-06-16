import numpy as np
graph=np.array([[1,0,0],[0,1,0],[0,0,0]])
PR=[1.0,1,0,1.0]
d=0.85
PRold=[99,99,99]

def calcPageRank(graph, PR):
    for i in range(len(graph)):
        sum=0
        for j in range(len(graph[i])):
            if graph[j,i]==1:
                sum+=PR[j]/len([n for n in graph[j] if n==1])
        PR[i]=(1-d)+(d*sum)
    return PR
for i in range(8):
    t=calcPageRank(graph, PR)
    print(t)
