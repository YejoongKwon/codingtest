def string_matching(T,P):
    cnt = 0
    n = len(T)
    m = len(P)
    for i in range(n-m+1):
        j = 0
        while j<m and P[j]==T[i+j]:
            j+=1
        if j==m:
            cnt +=1
    if cnt !=0:
        return 1, cnt
    else: return -1
def distance(p1, p2):
    import math
    return math.sqrt((p1[0]-p2[0])**2+((p1[1]-p2[1])**2))
def closest_pair(p):
    n = len(p)
    if n<2:
        return -1
    mindist = distance(p[0],p[1])
    cur1, cur2=0,1
    for i in range(n-1):
        for j in range(i+1, n):
            curdist = distance(p[i], p[j])
            if curdist < mindist:
                mindist = curdist
                cur1, cur2 = i,j
    return mindist, cur1, cur2

def dfs_stack(graph,start):
    visited = set()
    stack = [start]
    while stack:
        v = stack.pop()
        if v not in visited:
            visited.add(v)
            print(v, end='')
            for nbr in sorted(graph[v]-visited,reverse=True):
                stack.append(nbr)
    return visited

def dfs_recursive(graph,start,visited):
    if start not in visited:
        visited.add(start) # 방문 체크
        print(start,end='') # 방문 노드 출력
        nbr = graph[start]-visited # 아직 방문 안한 이웃 집합
        for v in nbr:
            dfs(graph, v, visited)

def bfs_queue(graph, start):
    import queue
    visited = set(start)
    que = queue.Queue()
    que.put(start)
    while not que.empty():
        v = que.get()
        print(v, end='')
        nbr = graph[v] - visited
        for u in nbr:
            visited.add(u)
            que.put(u)


def select_sort(word):
    word = list(word)
    n = len(word)

    for i in range(n-1):
        lst = i
        for j in range(i+1, n):
            if word[lst]>word[j]:
                lst = j

        word[i], word[lst] = word[lst], word[i]

    return word
def bubble_sort(word):
    word = list(word)
    for i in range(len(word)):
        for j in range(0,len(word)-i-1):
            if word[j] > word[j+1]:
                temp = word[j]
                word[j] = word[j+1]
                word[j+1]= temp
    return word

def binary_search(array, target):
    low = 0
    high = len(array)-1
    while low <= high:
        mid = low + (high-low)//2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            low = mid+1
        else:
            high = mid-1
    return -1

def binary_search_ver2(arr, key, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    mid = low +(high-low)//2

    if low > high:
        return -1

    else:
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            return binary_search_ver2(arr, key, low+1, high)
        else:
            return binary_search_ver2(arr, key, low, high-1)

