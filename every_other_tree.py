def num_of_leaves(S,G):
    num_leaves=0
    for v in S:
        if G.degree()[v]==1:
            num_leaves+=1
    return num_leaves

def remove_teo(G,y,l):
    G.plot(save_pos=True)
    pos_dict = G.get_pos()
    G.show(pos=pos_dict,vertex_colors={'blue':[],'red':[]})
    G.show(pos=pos_dict,vertex_colors={'blue':[],'red':y.support()})
    next_vertices=[l]
    S=set(next_vertices)
    G.show(vertex_colors={'blue':list(S),'red':list(set(y.support()).difference(S))})
    stop=False
    max_neighborhood=2
    while not stop:
        vertices=copy(next_vertices)
        next_vertices=[]
        for vertex in vertices:
            max_neighborhood+=max(0,len(G.adjacency_matrix()[vertex].support())-2)
            for neighbor in G.adjacency_matrix()[vertex].support():
                for u in G.adjacency_matrix()[neighbor].support():
                    if sign(y[u]) == -sign(y[vertex]):
                        vprime=u
                next_vertices.append(vprime)
        S.update(set(next_vertices))
        G.show(pos=pos_dict,vertex_colors={'blue':list(S),'red':list(set(y.support()).difference(S))})
        if num_of_leaves(S,G)==max_neighborhood:
            stop = True
    return(list(S))