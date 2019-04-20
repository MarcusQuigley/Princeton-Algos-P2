def powerOf(n):
  if (n==0): return 0
  if (n==1): return 1

  return n * powerOf(n-1)

def transposition(matrix, m,n):
  newmatrix = [[0 for x in range(m)] for x in range(n)]
  for row in range(len(matrix)):
    for column in range (len(matrix[row])):
      newmatrix[column][row] = matrix[row][column]
  
  return newmatrix
# matrix = [1,3,3,4,5,4,4,3,2,4,5,6,7,8,1]
# expected = [2,1,3,4,2,1,1,1]
# actual = histogram(matrix,9)


def histogram(array,m):
  map = {}
  result = [0] * m
  for i in array:
    if i in map:
      map[i]+=1
    else:
      map[i] = 1
  
  for k,v in map.items():
    result[k] = v

  return result


#Checking for cycle in graph using DFS
def course_schedule(numCourses, prerequisites):
  graph = [[] for _ in range(numCourses)]
  visited = [-1 for _ in range(numCourses)]

  for x,y in prerequisites:
    graph[x].append(y)

  def dfs(item):
    if visited[item] == 0: return False # currently being visited elsewhere so we have a cycle
    if visited[item] == 1:return True
    visited[item] = 0
    adjacents = graph[item]
    for i in adjacents:
      if not dfs(i):return False
    visited[item] = 1  
    return True

  for j in range(numCourses):
    if not dfs(j): return False
  return True

def topological_sort(n,data):
  #queue = []
  result_queue = []
  graph = [[] for _ in range(n)]
  for x,y in data:
    graph[x].append(y)
  #queue.append(data[0][0])
  
  def dfs(item):
    if item not in result_queue:
      adjacents = graph[item]
      if adjacents:
        for adj in adjacents:
          dfs(adj)
      result_queue.append(item)

  for i in range(n):
      dfs(i)
  
  return reversed(result_queue)


  


 


