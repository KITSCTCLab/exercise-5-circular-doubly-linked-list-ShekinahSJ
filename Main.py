class Node:
    def __init__(self, data=None):
        self.data = data
        self.previous = self
        self.next = self


class DoublyCircularLinkedList:
    def __init__(self):
        self.head = None
        self.end= None
        self.count = 0

    def add_at_tail(self, data) -> bool:
        # Write code here
        #Append a node of value data as the last element of the linked list. The function returns True after append operation.
        temp=Node(data)
        temp.previous=self.end
        #if list empty
        if (temp.end == None):
            self.head=temp
            self.tail=temp
            temp.next =None
        else:
            self.temp.next=temp
            temp.next=None
            self.tail=temp
        return True
    
    def add_at_head(self, data) -> bool:
        # Write code here
        '''Add a node of value data before the first element of the linked list. 
        After the insertion, the new node will be the first node of the linked list. 
        The function returns True after adding data at head.'''
        temp=Node(data)
        temp.next=temp.head
        if self.head != None:
            self.head.previous=temp
            self.head=temp
            temp.previous=None
        else:
            self.head=temp
            self.end=temp
            temp.previous=None
        return True

    def add_at_index(self, index, data) -> bool:
        # Write code here
        '''Add a node of value data before the indexth node in the linked list. 
        If index equals the length of the linked list, the node will be appended to the end of the linked list. 
        If index is greater than the length, the node will not be inserted. 
        If the operation is success, the function returns True, otherwise it returns False.'''

    def get(self, index) -> int:
        # Write code here
        #Get the value of the indexth node in the linked list. If the index is invalid, return -1.
        

    def delete_at_index(self, index) -> bool:
        # Write code here
        if index >= 0 and index < self.count:
            if index == 0:
                self.head.previous.next = self.head.next
                self.head.next.previous = self.head.previous
                self.head = self.head.next
                self.count -= 1
                return True
            elif index == self.count - 1:
                temp = self.head.previous
                temp.previous.next = temp.next
                temp.next.previous = temp.previous
                self.count -= 1
                return True
            else:
                temp = self.head
                for i in range(index):
                    temp = temp.next
                temp.previous.next = temp.next
                temp.next.previous = temp.previous
                self.count -= 1
                return True

        else:
            return False

    def get_previous_next(self, index) -> list:
        # Write code here
        if index >= 0 and index < self.count:
            l = []
            temp = self.head
            for i in range(index):
                temp = temp.next
            l.append(temp.previous.data)
            l.append(temp.next.data)
            return l
        else:
            return -1

    def display(self):
        temp=self.head
        print(self.count)
        for i in range (self.count):
            print(temp.data,"*",i)
            temp=temp.next

# Do not change the following code
operations = []
for specific_operation in input().split(','):
    operations.append(specific_operation.strip())
input_data = input()
data = []
iteration_count = 0

for item in input_data.split(', '):
    inner_list = []
    if item.isnumeric():
        data.append(int(item))
    elif item.startswith('['):
        item = item[1:-1]
        for letter in item.split(','):
            if letter.isnumeric():
                inner_list.append(int(letter))
        data.append(inner_list)

obj = DoublyCircularLinkedList()
result = []
for i in range(len(operations)):
    if operations[i] == "add_at_head":
        result.append(obj.add_at_head(data[i]))
    elif operations[i] == "add_at_tail":
        result.append(obj.add_at_tail(data[i]))
    elif operations[i] == "add_at_index":
        result.append(obj.add_at_index(int(data[i][0]), data[i][1]))
    elif operations[i] == "get":
        result.append(obj.get(data[i]))
    elif operations[i] == "get_previous_next":
        result.append(obj.get_previous_next(data[i]))
    elif operations[i] == 'delete_at_index':
        result.append(obj.delete_at_index(data[i]))

print(result)
