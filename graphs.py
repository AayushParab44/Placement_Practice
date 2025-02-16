graph_x={'A':['B'],'B':['C','D'],'C':['E','B','A'],'D':['E'],'E':['D','C']}

graph_x={'a':['c','b'],'b':['d'],'c':['e'],'d':['f'],'e':[],'f':[]} #abdfce

def dfs_graph(graph,root):
    stk=[root]
    while len(stk)!=0:
        popped=stk.pop()
        print(popped)
        stk.extend(graph[popped])


dfs_graph(graph_x,'a')

print()

def dfs_rec(graph,root):
    pass

