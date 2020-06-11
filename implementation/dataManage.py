import heapq

class Node():
    def __init__(self, state, parent):
        self.state = state
        self.parent = parent

class heapNode():                     #as heapq internally compare every element of tuple that's why comparision operator overloading is requried
    def __init__(self, state, parent, priority, steps):
        self.state = state
        self.parent = parent
        self.priority = priority
        self.steps = steps

    def __lt__(self,other):
        return self.priority < other.priority

    def __le__(self,other):
        return self.priority <= other.priority

    def __gt__(self,other):
        return self.priority > other.priority

    def __ge__(self,other):
        return self.priority >= other.priority

class stack():
    def __init__(self):
        self.frontier = []


    def isEmpty(self):
        if(len(self.frontier)==0):
            return True
        else:
            return False


    def insert(self,ele):
        self.frontier.append(ele)

    def remove(self):
        if(self.isEmpty()):
            raise Exception("Stack Underflow (i.e stack is empty)")

        else:
            node = self.frontier.pop()
            return node


class queue(stack):
    def remove(self):
        if(self.isEmpty()):
            raise Exception("Queue Underflow (i.e queue is empty)")

        else:
            node = self.frontier.pop(0)
            return node

class priorityq(stack):
    def insert(self,ele):
        heapq.heappush(self.frontier,ele)

    def remove(self):
        if(self.isEmpty()):
            raise Exception("Priority Queue is empty")

        else:
            node = heapq.heappop(self.frontier)
            return node
