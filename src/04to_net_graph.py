import ghpythonlib.components as ghc

class Graph(object):
    ''' 建立网络拓扑图，并建立获取节点（点），节点周边连通点和计算两点间值的方法'''
    def __init__(self, nodes, init_graph):
        self.nodes = nodes
        self.graph = self.construct_graph(nodes, init_graph)
        
    def construct_graph(self, nodes, init_graph):
        '''
        This method makes sure that the graph is symmetrical. In other words, if there's a path from node A to B with a value V, there needs to be a path from node B to node A with a value V.
        '''
        graph = {}
        for node in nodes:
            graph[node] = {}s
        
        graph.update(init_graph)
        
        for node, edges in graph.items():
            for adjacent_node, value in edges.items():
                if graph[adjacent_node].get(node, False) == False:
                    graph[adjacent_node][node] = value
                    
        return graph
    
    def get_nodes(self):
        "Returns the nodes of the graph."
        return self.nodes
    
    def get_outgoing_edges(self, node):
        "Returns the neighbors of a node."
        connections = []
        for out_node in self.nodes:
            if self.graph[node].get(out_node, False) != False:
                connections.append(out_node)
        return connections
    
    def value(self, node1, node2):
        "Returns the value of an edge between two nodes."
        return self.graph[node1][node2]
        
def connectivity_distance(pts,connectivity,weight=None):
    '''
    给定点列表、拓扑结构和权重（option）计算网络图

    Parameters
    ----------
    pts : list(Point3d)
        点列表.
    connectivity : Tree(int)
        点之间的连通关系.
    weight : list(float), optional
        距离权重值列表. The default is None.

    Returns
    -------
    graph : Class Instance
        包含网络图信息的类实例.

    '''

    #这一步要保障，输入为树型数据
    paths=connectivity.Paths
    
    init_graph={}
    nodes=[]
    for i,path in enumerate(paths):
        nodes.append(i)
        init_graph[i]={}
        pt=pts[i]
        pt_connectivity=connectivity.Branch(path)
        #print(pt_connectivity)
        for j in pt_connectivity:
            #print(j)
            pt_neighbor=pts[j]
            distance=ghc.Distance(pt,pt_neighbor)
            if weight:
                distance*=weight[i]
            init_graph[i][j]=distance
    #print(init_graph)
    graph=Graph(nodes,init_graph)
    
    return graph

if __name__=="__main__":
    graph=connectivity_distance(points,topology_connectivity,weight)