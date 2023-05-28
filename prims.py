INF = 9999999

n = int(input("Enter the number of vertices:\n"))

G=[]
print("Enter the adjacency matrix:\n")

for _ in range(n):
    row = list(map(int,input().split()))
    G.append(row)
    
selected_node = [False]*n
selected_node[0]= True
no_edges =0
MST=[]

print("Edge: Weight\n")
while (no_edges<n-1):
     min = INF
     a=-1 
     b=-1
     
     for i in range(n):
         if selected_node[i]:
             for j in range(n):
                 if not selected_node[j] and G[i][j]:
                     if G[i][j]<min:
                         min = G[i][j]
                         a =i
                         b=j
                         
     if (a!=-1)and(b!=-1):
         selected_node[b]= True
         no_edges+=1
         MST.append((a,b))
                     
                     
print("MST is:\n")
for edge in MST:
    a,b=edge
    print(f"{a}-{b}:{G[a][b]}")