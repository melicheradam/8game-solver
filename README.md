# 8game-solver

## TODO
 - [] translate code to english

Python script to solve the 8 tile game, start state and end state can both be defined. Each game state is represented as a string of numbers like "123456780", where 0 represents the empty tile. It calculates solvability by doing parity check for given input. 

To solve this problem, BFS algorithm is implemented. BFS has O(b<sup>d</sup>) time complexity, where b is branching factor and d is maximal tree depth - which are 3 and 31 in this case. This can be optimized by running 2 separate BFS, one from start state and another from end state. This reduces the time complexity to O(b<sup>d/2</sup>+b<sup>d/2</sup>), but introduces intesection checking to check if the trees have a common element.

When using FIFO stack to traverse the tree, intersection checking has O(m\*n) time complexity. This can be optimized by using sorted arrays to store processed game states, which gives us O(m+n). But using hashmaps, we can achieve O(m) time complexity (we need to check all elements of one tree).


![obrázok](https://user-images.githubusercontent.com/20504361/154839361-29d5a86f-07bb-4561-8927-a1f66bfe5a14.png) <br>
\*typ0 - FIFO, typ2 - sorted arrays, typ3 - hashmap <br>
\*\*y-axis - time in seconds, x-axis - number of moves to solve the game
