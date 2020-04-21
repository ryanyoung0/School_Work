# Ryan Young
# CSE CSE3500
# Zombie Outbreak Homework

def txt_to_list(txt_file_path, edges, vertices): # this function pulls from a text file path and returns three lists, one for the distances, one for the undirected edges and one for the vertices
    f = open(txt_file_path, "r")# need to pull from text file and create a list of lists
    file_lines = f.readlines() # reading all the lines in the txt file
    for line in file_lines:  # for each line in the list of lines that f.readlines() makes
        edges.append(tuple(line.split())) # cut off last two chars and convert to a list of strings
        vertices.append(line[:-2].split()[0]) # ^^ but only take the first element of that converted list
    second_half_edges = [] # so we can make the graph undriected we need to account for the reverse edges
    for edge in edges: # make the list of edges undirected
        second_half_edges.append([edge[1], edge[0], edge[2]]) # reversing
    edges = edges + second_half_edges # making a master list of undirected edges
    vertices = set(vertices) # make sure we dont have any duplciates
    for edge in second_half_edges:
        vertices.add(edge[0]) # add the rest of the vertices
    vertices = list(vertices) # change the set to a list now because we now know that there are no duplicates
    return vertices, edges # return the two lists"which is", days[1],

class Queue:
    def __init__(self):
        self.items = []

    def empty(self): # checks if the queue is empty
        return self.items == []

    def put(self, item): # puts an element in the queue
        self.items.insert(0,item)

    def get(self): # get an element from the queue
        return self.items.pop()

    def size(self): # return the size of the queue
        return len(self.items)

class Undirected_Graph:
    def __init__(self, V, E):
        self.neighbors = [] # create the list of lists
        self.num_vertices = 0
        self.vertices = V
        for vertex in V:# make each list in the list start with the name of the city leaving from
            self.neighbors.append([vertex])
            self.num_vertices += 1
        for vertex in self.neighbors:
            for e in E:
                if e[0] == vertex[0]:
                    vertex.append(e[1])

    def return_neighbors(self, v): # returns the neighbors of a vertex as a graph
        for vertex in self.neighbors:
            if vertex[0] == v:
                return vertex[1:]

    def print_neighbors(self): # print the adjanccey list otherwise know as the list named neighbors
        print(self.neighbors)

    def distance_between(self, edges, start, end): # retuns the distance between to cities given the start city as a string and the end city as a string
        for edge in edges:
            if start == edge[0] and end == edge[1]:
                return(int(edge[2]))

    def get_num_vertex(self): # return the number of vertices in the graph
        return self.num_vertices

    def get_vertices(self): # returns the list of vertices for the graph
        return self.vertices

    def dijkstra(self, edges, source):
        q = Queue()
        un_visited = set()
        dist = [] # list for the distances
        for vertex in self.get_vertices(): # initialize all weights in the graph to be infinity for all vertices
            if source == vertex:
                d = 0
                un_visited.add(source)
            else: # not the same vertex as the source
                d = float('inf')
                un_visited.add(vertex) # if the node is not the source node it is not visited yet
            dist.append([vertex, d]) # make a list of the (source , vertex), distance
        q.put(source) # put the source node into the Queue
        while not q.empty(): # while the queue is not empty
            x = q.get() # get the first object from the queue
            neighbors = self.return_neighbors(x) # grab the nieghbors of the current node
            if x in un_visited: # check if it has been visited yet
                un_visited.remove(x) # remove that neighbor for the unvisted list
                for d in dist: # for each distance in the distances list
                    if x == d[0]: # find our current node
                        current_distance = d[1]
                for n in neighbors: # for each neighbor of source
                    q.put(n) # put the un_visted neeighbor into the queue
                    #update each neighbors distance
                    for d in dist: # for each distance in the distance list
                        if n == d[0]: # if we get to the proper distance
                            old = d[1] # old neighbors distance
                            d[1] = min(old, current_distance + self.distance_between(edges, x, n)) # replace the old distance if the new one (length of edge plus current distance)
        return dist, source

def format(L, source): # format function to print a pretty output
    L.sort() # sort the list aplhabetically
    for city in L: # for each city in the list
        days = city[1] // 24 # convert time to days
        hours = city[1] % 24 # covnert time to hours
        print("The time it takes for the zombies to travel", city[1], "miles to get from", source, "to", city[0], "is:", days, "days", hours, "hours") # make it print prettu

def main(txt_file_path): # main function
    edges = [] # list of lists for the edges and their weights
    vertices = [] # a list of all vertexs
    distances = [] # a list of city and distance away from starting city
    vertices, edges = txt_to_list(txt_file_path, [], []) # wil take in a path and print the edges
    # need to take the list of edges ( that is directed right now) and conervet
    # to an unidrected graph object
    UG = Undirected_Graph(vertices, edges) # create an instance of the graph
    #n = UG.return_neighbors('Fargo') # testing to see if the retun negihbors method works
    #UG.distance_between(edges, 'Fargo', 'Hartford') # testing to see if the distance between method works
    #UG.print_neighbors()
    distances, source = UG.dijkstra(edges,'Hartford') # start dijsktras on the graph we implemented above, its edges, and a start which in this case is phoenix
    format(distances, source) # formatting the print out put to make it pretty


main("C:/Users/ryans/Documents/CSE3500/zombie_data.txt") # main function takes a path to the txt file that contains the city pairings and their distances
