class Node_web():

    def __init__(self,page= None,value = None,value2 = None,next = None,previous=None):
        self.page = page
        self.Next = next
        self.previous = previous
        self.value = value
        self.value2 = value2



    def __str__(self):
        return str(self.page)

    def reset(self):
        self.page = None
        self.Next = None
        self.previous = None
        self.value = None
        self.value2 = None
