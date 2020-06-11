import mazeManage as maz
import dataManage
import random
import pygame
from time import sleep
import pdb



# column_width = 60
# maze_size = (10,10)
# wall_width = 6

column_width = 6
maze_size = (100,100)
wall_width = 2

purple = (139, 120, 230)
light_purple = (178, 165, 240)
dark_purple = (105, 84, 209)
gray = (54,54,54)
bright_yellow = (250, 236, 10)
light_yellow = (255, 246, 107)

pygame.init()

#create the screen
screen = pygame.display.set_mode((1000,601))

base_maze = maz.emptyMaze(maze_size)
base_state = True

#game clock
clock = pygame.time.Clock()

#for game logo
logo = pygame.image.load("logo.png")
pygame.display.set_icon(logo)

def mainMenu():
    intro = True

    while intro:
        screen.fill(gray)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        largeText = pygame.font.Font('CabinSketch-Bold.ttf',73)
        title = largeText.render("MAZE Generator/Solver",True,purple)
        screen.blit(title,(120,100))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        # print(mouse)
        medText = pygame.font.Font('BalsamiqSans-BoldItalic.ttf',73)
        if(buttonClick("Lets Start",300,320,400,100,12,medText)):
            screen.fill(gray)

            largeText = pygame.font.Font('CabinSketch-Bold.ttf',73)
            title = largeText.render("Generating MAZE.....",True,purple)
            screen.blit(title,(120,250))
            pygame.display.update()
            mainGame(maz.createMaze(maze_size))

        pygame.display.update()

        clock.tick(20)





def drawMaze(maze,erase):

    for j in range(maze_size[0]):
        for i in range(maze_size[1]):
            x = j*column_width
            y = i*column_width
            pygame.draw.rect(screen, light_purple,[x,y,column_width,column_width])
            neighbors_avail = maze[(i,j)]

            if((i-1,j) not in neighbors_avail):
                pygame.draw.line(screen, dark_purple,(x,y),(x+column_width,y),wall_width)

            if((i,j+1) not in neighbors_avail):
                pygame.draw.line(screen, dark_purple,(x+column_width,y),(x+column_width,y+column_width),wall_width)

            if((i+1,j) not in neighbors_avail):
                pygame.draw.line(screen, dark_purple,(x+column_width,y+column_width),(x,y+column_width),wall_width)

            if((i,j-1) not in neighbors_avail):
                pygame.draw.line(screen, dark_purple,(x,y+column_width),(x,y),wall_width)
            pygame.display.update()
            if(not erase):
                clock.tick(480)
                # clock.tick(10)
    sleep(0.5)



def drawPath(maze,maze_sol):

    for ele in maze_sol:
        i = ele[0]
        j = ele[1]
        x = j*column_width
        y = i*column_width
        pygame.draw.rect(screen, light_yellow,[x,y,column_width,column_width])
        neighbors_avail = maze[(i,j)]

        if((i-1,j) not in neighbors_avail):
            pygame.draw.line(screen, dark_purple,(x,y),(x+column_width,y),wall_width)

        if((i,j+1) not in neighbors_avail):
            pygame.draw.line(screen, dark_purple,(x+column_width,y),(x+column_width,y+column_width),wall_width)

        if((i+1,j) not in neighbors_avail):
            pygame.draw.line(screen, dark_purple,(x+column_width,y+column_width),(x,y+column_width),wall_width)

        if((i,j-1) not in neighbors_avail):
            pygame.draw.line(screen, dark_purple,(x,y+column_width),(x,y),wall_width)
        pygame.display.update()
        clock.tick(480)
        # clock.tick(10)
    sleep(0.5)





def buttonClick(msg,x,y,w,h,button_width,text):

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if ((x < mouse[0] < x+w) and (y < mouse[1] < y+h)):

        pygame.draw.rect(screen,light_purple,[x,y,w,h])
        pygame.draw.rect(screen,gray,[x+button_width,y+button_width,w-(2*button_width),h-(2*button_width)])
        # medText = pygame.font.Font('BalsamiqSans-BoldItalic.ttf',73)
        # title = text.render("Lets Start",True,purple)
        title = text.render(msg,True,light_purple)
        titleRect = title.get_rect()
        titleRect.center = ( (x+(w//2)), (y+(h//2)) )
        screen.blit(title, titleRect)
        # screen.blit(title,(340,330))

        if click[0] == 1:
            return True

    else:
        pygame.draw.rect(screen,purple,[x,y,w,h])
        pygame.draw.rect(screen,gray,[x+button_width,y+button_width,w-(2*button_width),h-(2*button_width)])
        # medText = pygame.font.Font('BalsamiqSans-BoldItalic.ttf',73)
        # title = text.render("Lets Start",True,light_purple)
        title = text.render(msg,True,purple)
        titleRect = title.get_rect()
        titleRect.center = ( (x+(w//2)), (y+(h//2)) )
        screen.blit(title, titleRect)
        # screen.blit(title,(340,330))

    return False



def manhattanDistance(curr, goal):
    return(abs(curr[0]-goal[0])+abs(curr[1]-goal[1]))




def depthFirstSearch(maze):

    mazeFrontier = dataManage.stack()

    goal = (maze_size[0]-1,maze_size[1]-1)

    neighbors = []                             #store neighbors of each explored node
    node = dataManage.Node((0,0),None)                               #initial state
    explored = []                          #empty explored states except of first state

    # pdb.set_trace()

    mazeFrontier.insert(node)             #starting from first block of the maze from top left

    while(not mazeFrontier.isEmpty()):

        node = mazeFrontier.remove()

        if(node.state == goal):
            result = []
            while(node.parent != None):
                result.append(node.state)
                node = node.parent

            result.append(node.state)
            result.reverse()
            return result



        neighbors = maze[node.state]

        front_states = []                                   #elements states that are already in frontier
        for element in mazeFrontier.frontier:
            front_states.append(element.state)

        explored_states = []                                 #element state in explored
        for element in explored:
            explored_states.append((element.state))


        neighbors = list((set(neighbors)-set(explored_states))-set(front_states))      #to remove already visited neighbors
                                                            #   from the "neighbors" list

        explored.append(node)
        for ele in neighbors:
            next_node = dataManage.Node(ele,node)
            mazeFrontier.insert(next_node)

    return None


def greedyBestFirstSearch(maze):

    mazeFrontier = dataManage.priorityq()

    goal = (maze_size[0]-1,maze_size[1]-1)

    neighbors = []                             #store neighbors of each explored node
    node = dataManage.heapNode((0,0),None,manhattanDistance((0,0),goal),None)                             #initial state
    explored = []                          #empty explored states except of first state

    # pdb.set_trace()

    mazeFrontier.insert(node)             #starting from first block of the maze from top left

    while(not mazeFrontier.isEmpty()):

        node = mazeFrontier.remove()

        if(node.state == goal):
            result = []
            while(node.parent != None):
                result.append(node.state)
                node = node.parent

            result.append(node.state)
            result.reverse()
            return result



        neighbors = maze[node.state]

        front_states = []                                   #elements states that are already in frontier
        for element in mazeFrontier.frontier:
            front_states.append(element.state)

        explored_states = []                                 #element state in explored
        for element in explored:
            explored_states.append((element.state))


        neighbors = list((set(neighbors)-set(explored_states))-set(front_states))      #to remove already visited neighbors
                                                            #   from the "neighbors" list

        explored.append(node)
        for ele in neighbors:
            next_node = dataManage.heapNode(ele,node,manhattanDistance(ele,goal),None)
            mazeFrontier.insert(next_node)
            # print(mazeFrontier.frontier,"\n")


    return None

def aStarSearch(maze):

    mazeFrontier = dataManage.priorityq()

    goal = (maze_size[0]-1,maze_size[1]-1)

    neighbors = []                             #store neighbors of each explored node
    node = dataManage.heapNode((0,0),None,manhattanDistance((0,0),goal),0)                             #initial state
    explored = []                          #empty explored states except of first state

    # pdb.set_trace()

    mazeFrontier.insert(node)             #starting from first block of the maze from top left

    while(not mazeFrontier.isEmpty()):

        node = mazeFrontier.remove()

        if(node.state == goal):
            result = []
            while(node.parent != None):
                result.append(node.state)
                node = node.parent

            result.append(node.state)
            result.reverse()
            return result



        neighbors = maze[node.state]

        front_states = []                                   #elements states that are already in frontier
        for element in mazeFrontier.frontier:
            front_states.append(element.state)

        explored_states = []                                 #element state in explored
        for element in explored:
            explored_states.append((element.state))


        neighbors = list((set(neighbors)-set(explored_states))-set(front_states))      #to remove already visited neighbors
                                                            #   from the "neighbors" list

        explored.append(node)
        for ele in neighbors:
            step = node.steps + 1
            next_node = dataManage.heapNode(ele,node,manhattanDistance(ele,goal)+step,step)
            mazeFrontier.insert(next_node)
            # print(mazeFrontier.frontier,"\n")


    return None


def dijkstraSearch(maze):

    mazeFrontier = dataManage.priorityq()

    goal = (maze_size[0]-1,maze_size[1]-1)

    neighbors = []                             #store neighbors of each explored node
    node = dataManage.heapNode((0,0),None,0,0)                             #initial state
    explored = []                          #empty explored states except of first state

    # pdb.set_trace()

    mazeFrontier.insert(node)             #starting from first block of the maze from top left

    while(not mazeFrontier.isEmpty()):

        node = mazeFrontier.remove()

        if(node.state == goal):
            result = []
            while(node.parent != None):
                result.append(node.state)
                node = node.parent

            result.append(node.state)
            result.reverse()
            return result



        neighbors = maze[node.state]

        front_states = []                                   #elements states that are already in frontier
        for element in mazeFrontier.frontier:
            front_states.append(element.state)

        explored_states = []                                 #element state in explored
        for element in explored:
            explored_states.append((element.state))


        neighbors = list((set(neighbors)-set(explored_states))-set(front_states))      #to remove already visited neighbors
                                                            #   from the "neighbors" list

        explored.append(node)
        for ele in neighbors:
            step = node.steps + 1
            next_node = dataManage.heapNode(ele,node,step,step)
            mazeFrontier.insert(next_node)
            # print(mazeFrontier.frontier,"\n")


    return None


def breadthFirstSearch(maze):

    mazeFrontier = dataManage.queue()

    goal = (maze_size[0]-1,maze_size[1]-1)

    neighbors = []                             #store neighbors of each explored node
    node = dataManage.Node((0,0),None)                               #initial state
    explored = []                          #empty explored states except of first state

    # pdb.set_trace()

    mazeFrontier.insert(node)             #starting from first block of the maze from top left

    while(not mazeFrontier.isEmpty()):

        node = mazeFrontier.remove()

        if(node.state == goal):
            result = []
            while(node.parent != None):
                result.append(node.state)
                node = node.parent

            result.append(node.state)
            result.reverse()
            return result



        neighbors = maze[node.state]

        front_states = []                                   #elements states that are already in frontier
        for element in mazeFrontier.frontier:
            front_states.append(element.state)

        explored_states = []                                 #element state in explored
        for element in explored:
            explored_states.append((element.state))


        neighbors = list((set(neighbors)-set(explored_states))-set(front_states))      #to remove already visited neighbors
                                                            #   from the "neighbors" list

        explored.append(node)
        for ele in neighbors:
            next_node = dataManage.Node(ele,node)
            mazeFrontier.insert(next_node)

    return None




def mainGame(maze):
    screen.fill(gray)
    sleep(0.5)
    pygame.display.update()


    drawMaze(maze,False)
    # print(maze)

    solution = None

    while True:


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        text = pygame.font.Font('BalsamiqSans-BoldItalic.ttf',48)
        title = text.render("Solve Maze With",True,purple)
        screen.blit(title,(615,70))

        text = pygame.font.Font('BalsamiqSans-BoldItalic.ttf',30)



        if(buttonClick("Depth First Search",630,140,350,50,2,text)):

            if(solution != None):
                drawMaze(maze,True)
                sleep(0.5)
            solution = depthFirstSearch(maze)
            # print(solution)
            drawPath(maze,solution)

        if(buttonClick("Breadth First Search",630,210,350,50,2,text)):
            if(solution != None):
                drawMaze(maze,True)
                sleep(0.5)
            solution = breadthFirstSearch(maze)
            # print(solution)
            drawPath(maze,solution)

        if(buttonClick("Greedy Best First Search",630,280,350,50,2,text)):
            if(solution != None):
                drawMaze(maze,True)
                sleep(0.5)
            solution = greedyBestFirstSearch(maze)
            # print(solution)
            drawPath(maze,solution)

        if(buttonClick("A* Search",630,350,350,50,2,text)):
            if(solution != None):
                drawMaze(maze,True)
                sleep(0.5)
            solution = aStarSearch(maze)
            # print(solution)
            drawPath(maze,solution)

        if(buttonClick("Dijkstra Search",630,420,350,50,2,text)):
            if(solution != None):
                drawMaze(maze,True)
                sleep(0.5)
            solution = dijkstraSearch(maze)
            # print(solution)
            drawPath(maze,solution)

        if(buttonClick("EXIT",630,510,350,50,2,text)):
            exit()

        pygame.display.update()
        clock.tick(30)





if __name__ == "__main__":
    mainMenu()
