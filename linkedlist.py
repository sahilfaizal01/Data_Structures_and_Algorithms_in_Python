class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next
    
class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert_at_beginning(self,data):
        node = Node(data,self.head)
        self.head = node
    
    def print_ll(self):
        if self.head is None:
            print('Linked List is Empty')
            
        llstr = ''
        itr = self.head
        
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        
        print(llstr)
    
    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data,None)
        
    def insert_values(self,values):
        self.head = None
        for val in values:
            self.insert_at_end(val)
    
    def count_nodes(self):
        itr = self.head
        count = 0
        while itr:
            count+=1
            itr = itr.next
        return count
    
    def remove_at(self,index):
        if index<0 or index>=self.count_nodes():
            raise Exception('Invalid Index')
        
        if index == 0: # remove from beginning
            self.head = self.head.next
            return
        
        cnt = 0
        itr = self.head
        while itr:
            if cnt == index-1:
                itr.next = itr.next.next
                break  
            itr = itr.next
            cnt+=1
    
    def insert_at_index(self,data,index):
        if index<0 or index>self.count_nodes():
            raise Exception('Invalid Index')
        
        if index==0:
            self.insert_at_beginning(data)
            return
        
        cnt = 0
        itr = self.head
        while itr:
            if cnt == index-1:
                node = Node(data,itr.next)
                itr.next = node
                break
            itr = itr.next
            cnt+=1
    
    def insert_after_value(self,val,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        
        idx = 0
        itr = self.head
        while itr:
            if itr.data == val:
                break
            itr = itr.next
            idx+=1
        self.insert_at_index(data,idx+1)      
        
    def remove_after_values(self,val):
        idex = 0
        itr = self.head
        while itr:
            if itr.data == val:
                break
            itr = itr.next
            idex+=1
        self.remove_at(idex+1)
        
            

if __name__ == '__main__':
    l = LinkedList()
    # l.insert_at_beginning(10)
    # l.insert_at_beginning(5)
    # l.insert_at_end(15)
    # l.insert_at_end(20)
    l.insert_values(['mango','apple','orange','grapes'])
    l.print_ll()
    l.insert_after_value('orange','banana')
    l.print_ll()
    l.remove_after_values('banana')
    l.print_ll()