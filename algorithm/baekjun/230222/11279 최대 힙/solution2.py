import sys
sys.stdin = open('input.txt', encoding='UTF-8')
input = sys.stdin.readline

class MaxHeap:
    def __init__(self):
        self.heap = []
    
    def push(self, x):
        self.heap.append(x)
        i = len(self.heap) - 1
        while i > 0 and self.heap[i] > self.heap[(i - 1) // 2]:
            self.heap[i], self.heap[(i - 1) // 2] = self.heap[(i - 1) // 2], self.heap[i]
            i = (i - 1) // 2
    
    def pop(self):
        if not self.heap:
            return 0
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        i = 0
        while 2 * i + 1 < len(self.heap):
            if 2 * i + 2 == len(self.heap) or self.heap[2 * i + 1] > self.heap[2 * i + 2]:
                j = 2 * i + 1
            else:
                j = 2 * i + 2
            if self.heap[j] > self.heap[i]:
                self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
                i = j
            else:
                break
        return root

max_heap = MaxHeap()
n = int(input())
for i in range(n):
    x = int(input())
    if x == 0:
        print(max_heap.pop())
    else:
        max_heap.push(x)

'''
완전 이진 트리를 구현하여 최대 힙을 나타낸 모습이다.
물론 내가 한 건 아니고 chatGPT 가 잘 만들어주었다.
대단한 녀석이다...
'''