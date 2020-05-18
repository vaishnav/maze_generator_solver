class Node():
    def __init__(self, state, parent):
        self.state = state
        self.parent = parent

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
