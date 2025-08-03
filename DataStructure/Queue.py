class Queue:
    def __init__(self):
        self.container = list()

    def empty(self):
        if not self.container:
            return True
        else:
            return False

    def enqueue(self, data):
        self.container.append(data)

    def dequeue(self, data):
        return self.container.pop(0)
   #동적 배열의 맨 처음 데이터 삭제 : 최악의 경우 O(n)
    #좀더 효율적으로 구현?

    
    def peek(self):
        return self.container[0]