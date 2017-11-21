from Node_web import  *

class keepHistory():

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def keep_page(self,page,value = None,value2 = None):
        page = Node_web(page,value,value2)
        if self.size == 0:
            self.head = page
            self.tail = page
            self.size += 1
        else:
            page.previous = self.tail
            self.tail.Next = page
            self.tail = page
            self.size += 1

    def history(self):
        if self.size == 0:
            pass
        elif self.size == 1:
            name_page = self.tail.page
            return name_page
        elif self.size > 1:
            Node_page = self.tail
            self.tail = Node_page.previous
            self.tail.Next = None
            Node_page.previous = None
            self.size -= 1
            name_page = self.tail.page
            return name_page

    def Value_page(self):
        return self.tail.value

    def Value2_page(self):
        return self.tail.value2

    def reset_keepHistory(self):
        self.head = None
        self.tail = None
        self.size = 0


    def print_listPage(self):
        page = self.head
        while page:
            print(page.page)
            print(page.value)
            page = page.Next
