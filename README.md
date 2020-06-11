# maze_generator_solver

Generating non-perfect mazes and solving them with different algorithms (GUI)
___


## About Project
Maze is generated using recursive backtracking([Maze generating algorithms](https://en.wikipedia.org/wiki/Maze_generation_algorithm)) and than randomly erasing walls between blocks to generate non-perfect maze
___

## how it looks
![elementary](https://github.com/vaishnav/maze_generator_solver/blob/master/demo/Screenshot.png)

## Implemented So far
1. Depth First Serach
2. Breadth First Search
3. Greedy Best first Search
4. A* algorithms
5. Dijkstra (note: as the maze here is in the form of unweighted graph dijkstra will work like Breadth First Search and performance would be lower than actual BFS)
___



## How to use

### Install the dependencies
```
pip3 install -r requirements.txt
```
```
cd location/implementation/
python3 mazeGen.py
```
