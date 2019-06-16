import numpy as np
import math

graph=np.array([[0,0,1],[1,0,1],[0,0,0]])
hub_wt=np.array([1.0,1.0,1.0])
auth_wt=np.array([1.0,1.0,1.0])

def norm(x):
    sum=0
    for i in range(len(x)):
        sum+=x[i]**2
    return math.sqrt(sum)

for k in range(3):
    for i in range(len(graph)):
        sum=0
        for j in range(len(graph[i])):
            if graph[j,i] ==1:
                sum+=hub_wt[j]
        auth_wt[i]=sum
    i=0
    for i in range(len(graph)):
        sum=0
        for j in range(len(graph[i])):
            if graph[i][j]==1:
                sum+=auth_wt[j]
        hub_wt[i]=sum
    print(auth_wt)
    print(hub_wt)
print("Normalised")
norm_Auth=norm(auth_wt)
norm_Hub=norm(hub_wt)
for j in range(0,len(auth_wt)):
    hub_wt[i]=hub_wt[i]/norm_Hub
    auth_wt[i]=auth_wt[i]/norm_Auth
print(hub_wt)
print(auth_wt)
