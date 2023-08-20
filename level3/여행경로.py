tickets = [
    ["ICN", "SFO"],
    ["ICN", "ATL"],
    ["SFO", "ATL"],
    ["ATL", "ICN"],
    ["ATL", "SFO"]]


def solution(tickets):
    graph = {}
    answer = []
    for start, end in tickets:
        if start not in graph:
            graph[start] = []
            graph[start].append(end)
        else:
            graph[start].append(end)
    for key in graph.keys():
        graph[key] = sorted(graph[key])

    print(graph)

    def dfs(s):
        while s in graph and graph[s]:
            dfs(graph[s].pop(0))

        if s not in graph:
            answer.append(s)
            return

        if not graph[s]:
            answer.append(s)
            return

    dfs("ICN")
    return answer[::-1]


#
# import collections
#
#
# def solution(tickets):
#     answer = []
#     graph = collections.defaultdict(list)
#
#     for a, b in tickets:
#         graph[a].append(b)
#     for a, b in graph.items():
#         graph[a].sort()
#
#     print(graph)
#
#     def dfs(s):
#         while graph[s]:
#             dfs(graph[s].pop(0))
#
#         if not graph[s]:
#             answer.append(s)
#             return
#
#     dfs("ICN")
#
#     return answer[::-1]


solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]])
