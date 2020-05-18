import dataManage
import random
import pdb                                   #for debugging



def neighbor_find(element, maze_size):       #find the neighbors of particular node
    neighbors = []
    x = element[0]
    y = element[1]

    if(x-1 >= 0):
        neighbors.append((x-1,y))

    if(x+1 < maze_size[0]):
        neighbors.append((x+1,y))

    if(y-1 >= 0):
        neighbors.append((x,y-1))

    if(y+1 < maze_size[1]):
        neighbors.append((x,y+1))

    return neighbors


# def neighbor_dir(ele,neighbor):
#     if(ele[0]-1 == neighbor[0]):
#         return "up"


def emptyMaze(maze_size):
    # using dict comprehension to genrate graph for maze
    maze = {(x,y):[] for x in range(maze_size[0]) for y in range(maze_size[1])}
    return maze



def createMaze(maze_size = (4,4)):

    maze = emptyMaze(maze_size)

    # create maze with the help of recursive backtracking
    mazeFrontier = dataManage.stack()      #stack for genrating maze


    neighbors = []                             #store neighbors of each explored node
    node = (0,0)                               #initial state
    explored = [node]                          #empty explored states except of first state

    # pdb.set_trace()

    mazeFrontier.insert(node)             #starting from first block of the maze from top left

    while(not mazeFrontier.isEmpty()):
        neighbors = neighbor_find(node,maze_size)

        neighbors = list((set(neighbors)-set(explored))-set(mazeFrontier.frontier))      #to remove already visited neighbors
                                                            #   from the "neighbors" list


        if(len(neighbors)==0):
            if(random.randint(1,20) > 18):                     #randomly joining two paths otherwise maze ganerated is perfect (perfect maze have only one solution)
                neigh = neighbor_find(node,maze_size)
                random_node = neigh[random.randint(0,len(neigh)-1)]

                maze[node].append(random_node)
                maze[random_node].append(node)
            node = mazeFrontier.remove()
            continue


        next_node = neighbors[random.randint(0,len(neighbors)-1)]
        maze[node].append(next_node)
        maze[next_node].append(node)
        mazeFrontier.insert(next_node)
        node = next_node
        explored.append(node)
    return maze




# def main(maze_size = (4,4)):
#     maze = createMaze(maze_size)
#     print(maze)

# if __name__ == "__main__":
#     main()
