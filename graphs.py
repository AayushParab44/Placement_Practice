graph_x={'A':['B'],'B':['C','D'],'C':['E','B','A'],'D':['E'],'E':['D','C']}

graph_x={'a':['c','b'],'b':['d'],'c':['e'],'d':['f'],'e':[],'f':[]} #abdfce

graph_x={'a':['b','c'],'b':['d'],'c':['e'],'d':['f'],'e':[],'f':[]} #abdfce

#     a
#    / \
#   b   c
#   |    \
#   d     e
#   |
#   f

def dfs_graph(graph,root):
    stk=[root]
    while len(stk)!=0:
        popped=stk.pop()
        print(popped)
        stk.extend(graph[popped])

# print('dfs using graph iteratively-')
# # dfs_graph(graph_x,'a')

# print()
# # print('dfs using graph recursively-')


def dfs_rec(graph,root):
    print(root)
    for i in graph[root]:
        dfs_rec(graph,i)

# dfs_rec(graph_x,'a')

#has_path recursively-
def rec_hasp(graph,root,val):
    if root==val: return True

    for i in graph[root]:
        if rec_hasp(graph,i,val)==True:return True
    
    return False
graph_x={'a':['b','c'],'b':['d'],'c':['e'],'d':['f'],'e':[],'f':[]} #abdfce
#To search for 'f' in the graph-
# print(rec_hasp(graph_x,'a','e'))

#has path using bfs-
def hp_bfs(graph,curr,val):
    q=[curr]
    
    while len(q)!=0:
        popped=q.pop()
        if popped==val: return True
        q.extend(q[popped])

    return False

# print(rec_hasp(graph_x,'a','r'))