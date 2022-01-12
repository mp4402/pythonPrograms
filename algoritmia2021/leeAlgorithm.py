import sys
import time
from memory_profiler import profile
from collections import deque
 
# Below lists detail all four possible movements from a cell
row = [-1, 0, 0, 1]
col = [0, -1, 1, 0]
 
 
# Function to check if it is possible to go to position (row, col)
# from the current position. The function returns false if row, col
# is not a valid position or has a value 0 or already visited.
def isValid(mat, visited, row, col):
    return (row >= 0) and (row < len(mat)) and (col >= 0) and (col < len(mat[0])) \
           and mat[row][col] == 1 and not visited[row][col]
 
 
# Find the shortest possible route in a matrix `mat` from source `src` to
# destination `dest`
@profile
def findShortestPathLength(mat, src, dest):
 
    # get source cell (i, j)
    i, j = src
 
    # get destination cell (x, y)
    x, y = dest
 
    # base case: invalid input
    if not mat or len(mat) == 0 or mat[i][j] == 0 or mat[x][y] == 0:
        return -1
 
    # `M × N` matrix
    (M, N) = (len(mat), len(mat[0]))
 
    # construct a matrix to keep track of visited cells
    visited = [[False for x in range(N)] for y in range(M)]
 
    # create an empty queue
    q = deque()
 
    # mark the source cell as visited and enqueue the source node
    visited[i][j] = True
 
    # (i, j, dist) represents matrix cell coordinates, and their
    # minimum distance from the source
    q.append((i, j, 0))
 
    # stores length of the longest path from source to destination
    min_dist = sys.maxsize
 
    # loop till queue is empty
    while q:
 
        # dequeue front node and process it
        (i, j, dist) = q.popleft()
 
        # (i, j) represents a current cell, and `dist` stores its
        # minimum distance from the source
 
        # if the destination is found, update `min_dist` and stop
        if i == x and j == y:
            min_dist = dist
            break
 
        # check for all four possible movements from the current cell
        # and enqueue each valid movement
        for k in range(4):
            # check if it is possible to go to position
            # (i + row[k], j + col[k]) from current position
            if isValid(mat, visited, i + row[k], j + col[k]):
                # mark next cell as visited and enqueue it
                visited[i + row[k]][j + col[k]] = True
                q.append((i + row[k], j + col[k], dist + 1))
 
    if min_dist != sys.maxsize:
        return min_dist
    else:
        return -1
 
 
if __name__ == '__main__':
 
    mat = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 1, 1, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
        [1, 0, 0, 1, 1, 0, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 0, 0, 0, 1, 0, 1, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 1, 1, 1, 1, 0, 0, 1, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 0, 1]
    ]
 
    src = (0, 0)
    dest = (9, 9)
    start_time = time.time()
    min_dist = findShortestPathLength(mat, src, dest)
 
    if min_dist != -1:
        print("The shortest path from source to destination has length", min_dist)
        print("Tiempo en ejecución: %s  segundos " %(time.time() - start_time))
    else:
        print("Destination cannot be reached from source")
        print("Tiempo en ejecución: %s  segundos " %(time.time() - start_time))
 