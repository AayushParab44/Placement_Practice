graph_x={'A':['B'],'B':['C','D'],'C':['E','B','A'],'D':['E'],'E':['D','C']}

graph_x={'a':['c','b'],'b':['d'],'c':['e'],'d':['f'],'e':[],'f':[]} #abdfce

graph_x={'a':['b','c'],'b':['d'],'c':['e'],'d':['f'],'e':[],'f':[]} #abdfce


def dfs_graph(graph,root):
    stk=[root]
    while len(stk)!=0:
        popped=stk.pop()
        print(popped)
        stk.extend(graph[popped])

print('dfs using graph iteratively-')
dfs_graph(graph_x,'a')

print()
print('dfs using graph recursively-')


def dfs_rec(graph,root):
    print(root)
    for i in graph[root]:
        dfs_rec(graph,i)

dfs_rec(graph_x,'a')
