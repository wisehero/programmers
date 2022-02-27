"""
 힙도 이진 트리의 한 종류다.
 루트 노드가 언제나 최댓값 또는 최솟값을 가진다.
 최대 힙과 최소 힙으로 구분이 가능하다.
 완전 이진 트리여야 힙이다.
"""


class MaxHeap:

    def __init__(self):
        self.data = [None]

    def insert(self, item):
        self.data.append(item)

        index = len(self.data) - 1

        while index != 1:
            numOfParentNode = index // 2
            print(numOfParentNode)

            if self.data[numOfParentNode] < self.data[index]:
                self.data[numOfParentNode], self.data[index] = self.data[index], self.data[numOfParentNode]
            else:
                break


def solution(x):
    return 0
