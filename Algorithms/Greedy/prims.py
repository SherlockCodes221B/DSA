'''
Data Structre used here is Graphs
'''



V = 5
G = [[0, 9, 75, 0, 0],
     [9, 0, 95, 19, 42],
     [75, 95, 0, 51, 66],
     [0, 19, 51, 0, 31],
     [0, 42, 66, 31, 0]]
selected = [0,0,0,0,0]
no_of_edges = 0
selected[0] = True
print("Edge : Weight \n")
minimum = 9999999
while (no_of_edges < V - 1):
    x = 0
    y = 0
    for i in range(V):
        if selected[i]:
            for j in range(V):
                if((not selected[j]) and G[i][j]):
                    if minimum > G[i][j]:
                        minimum = G[i][j]
                        x = i
                        y = j
    print(str(x) + "-" + str(y) + ":" + str(G[x][y]))
    selected[y] = True
    no_of_edges += 1
