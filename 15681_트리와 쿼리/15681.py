import sys
from sys import stdin
sys.setrecursionlimit(100010)

n, r, q = map(int, input().split())
graph = [ list() for _ in range(n+1) ]
child_list = [ list() for _ in range(n+1) ]
parent_node = [ 0 for _ in range(n+1) ]
size = [ 0 for _ in range(n+1)]

for _ in range(n-1):
    f, t = map(int, stdin.readline().strip().split())
    graph[f].append(t)
    graph[t].append(f)

def makeTree(currentNode, parent):
    for node in graph[currentNode]:
        if node != parent:
            child_list[currentNode].append(node)
            parent_node[node] = currentNode
            makeTree(node, currentNode)

def countSubtreeNodes(currentNode) :
    size[currentNode] = 1 # 자신도 자신을 루트로 하는 서브트리에 포함되므로 0이 아닌 1에서 시작한다.
    for Node in child_list[currentNode]:
        countSubtreeNodes(Node)
        size[currentNode] += size[Node]

makeTree(r, -1)
countSubtreeNodes(r)


for _ in range(q):
    target = int(stdin.readline().strip())
    print(size[target])

