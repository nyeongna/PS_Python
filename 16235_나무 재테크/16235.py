from sys import stdin
import sys
import copy

n, m, k = map(int, stdin.readline().strip().split())
nutrient = [ list(map(int, stdin.readline().strip().split())) for _ in range(n) ]
nutrient_graph = [ [5]*n for _ in range(n) ]
tree_graph = [ [ list() for _ in range(n) ] for _ in range(n) ]

for _ in range(m):
    x, y, age = map(int, stdin.readline().strip().split())
    tree_graph[x-1][y-1].append(age)

def SpringSummer():
    for i in range(n):
        for j in range(n):
            tree_graph[i][j].sort()
            alive_tree_list, dead_tree = [], 0
            for age in tree_graph[i][j]:
                if age <= nutrient_graph[i][j]:
                    alive_tree_list.append(age+1)
                    nutrient_graph[i][j] -= age
                else:
                    dead_tree += age//2
            nutrient_graph[i][j] += dead_tree
            tree_graph[i][j] = alive_tree_list

x_dir = [-1,0,1,0, -1, 1, 1, -1]
y_dir = [0,1,0,-1, 1, 1, -1, -1]

def Fall():
    for i in range(n):
        for j in range(n):
            for tree in tree_graph[i][j]:
                if tree%5 == 0:
                    for k in range(8):
                        dx = i+x_dir[k]
                        dy = j+y_dir[k]
                        if 0<=dx<n and 0<=dy<n:
                            tree_graph[dx][dy].append(1)

def Winter():
    for i in range(n):
        for j in range(n):
            nutrient_graph[i][j] += nutrient[i][j]

                
for time in range(k):
    SpringSummer()
    Fall()
    Winter()

ans = 0
for i in tree_graph:
    for j in i:
        ans = ans + len(j)
print(ans)
