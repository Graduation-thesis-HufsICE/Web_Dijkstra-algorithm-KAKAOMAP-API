#다익스트라 알고리즘 작성한 파이썬 파일
import heapq
import ast
import json
from collections import OrderedDict
import sys


def dijkstra(graph, start, end):  #탐색할 그래프/시점/종점
    distances = {vertex: [float('inf'), start] for vertex in graph}  #시점에서 각 정점까지의 거리를 저장할 딕셔너리 생성/무한대로 초기화
    distances[start] = [0, start] #그래프의 시점 거리는 0
    queue = []
    heapq.heappush(queue, [distances[start][0], start]) #시점과 시점의 거리를 최소힙에 추가
    
    while queue:
        current_distance, current_vertex = heapq.heappop(queue)
        if distances[current_vertex][0] < current_distance: #더 짧은 경로는 무시
            continue
        for adjacent, weight in graph[current_vertex].items(): #시점에서 인접 정점으로 바로 가는것보다 현재 정점을 통해 가는 것이 더 가까우면 거리를 업데이트
            distance = current_distance + weight
            if distance < distances[adjacent][0]:
                distances[adjacent] = [distance, current_vertex]
                heapq.heappush(queue, [distance, adjacent])

    path = end
    path_output = end
    while distances[path][1] != start:
        path_output += distances[path][1]
        path = distances[path][1]
    path_output += start
    return (', '.join(path_output[::-1]).strip())
    #return distances
    # return(path_output[::-1])


with open('graph.txt', 'r', encoding='utf-8') as result: #그래프를 나타낸 txt파일을 딕셔너리 형식으로 불러오기
    mygraph = ast.literal_eval(result.read())

start = input('출발지를 입력하세요. : ')
end = input('목적지를 입력하세요. : ')
print(dijkstra(mygraph, start, end), end='')

sys.stdout = open('route.txt', 'w', encoding='utf-8')
print(dijkstra(mygraph, start, end), end='')