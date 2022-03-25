#=========================================================================================================|
# Only use single-linked lists if you plan to delete, or insert an element                                                                                                                                  
# They save also save memory, because for deleting nodes, you just readjust the pointer, whereas in arrays                                                              
# you have to delete the element and double the space of the array by allocating new memory,
# and shift all elements to the right of the insert location. This takes a lot of memory, so this is where linked lists come in
#=========================================================================================================|


# The following code is implementation + explanation for single-linked lists
#It contains common methods for linked lists and a description of how they work


class Node(object):
    def __init__(self, value): #Attributes for each node, each node has a value and a pointer to the next node
        self.val = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None): #Initializes linked list
        self.head = head


     def appendItems(self, data): #Method to append values to linked list
        node = Node(data) #creates a node that holds specified data

        if self.head:               #checks if there is a head to the linked list, if yes, scan the linkedlist until u reach the final element
                                    #store the final element in a variable
                                    #set the pointer from the variable to the new addition to the list
            elem = self.head
            while elem != None:
                elem = elem.next
            elem.next = node #the true last element will now point to the value that must be added to the end of the list


        else:               #if there is no head of the linked list, set the head to the new element(Basically used when u are adding the first node to the linked list)
            self.head = node

     #The method above is the reason why you can use the node attributes in the linked list. Basically, for every value you pass to this method, a new node is created of that value, so for any method in this class, you can use the Node class attributes.
     #That node contains both the reference pointer and the value, so this method is what connects the head and the nodes together to form the list       

    def printElements(self):
        node = self.head
        res = ""
        while node != None: #Loop keeps running as long as the head isn't None type, that is, as long as the head exists
            if node.next == None:
                res+=node.val
                break
            res+=(f"{node.val} --> ")
            node = node.next
        print(res)#prints linked list


    def findSize(self): #Method that finds the size of the linked list
        size = 0
        elem = self.head
        while elem!=None: #iterates over the linked list and for each element, the size increments by 1
            size+=1
            elem = elem.next
        return size


    def findItem(self, data):
        elem = self.head
        while elem!=None:
            if elem.val == data: #If the value of the node equals the value passed to the method return True
                print(True)
            elem = elem.next
        print(False)


    def retItemAtIndex(self, index): #Basically, this method iterates over the list, and if the current position is 1 less than the index that needs to be found, return the value of the next index.
                                    #If the index passed is not in the list, return out of bounds exception
        elem = self.head
        pos = 0
        while elem!=None:
            if pos + 1 == index: 
                return elem.next.val
            elem=elem.next
            pos+=1
        return Exception('Index not found or index given was out of bounds')



    def setVal(self, index, value): #Basically, same logic as the method above, but instead of returning the value at that index, we set the value to the value passed to the method
        elem = self.head
        pos = 0
        while elem!=None:
            if pos + 1 == index:
                elem.next.val = value
                return 
            elem=head.next
            pos+=1
        raise Exception('Out of Bounds')


    def delItems(self, index):
        if index == 0: #If you want to delete the head, set the head to the next node of the linked list
            self.head = self.head.next
            return
        head = self.head
        count = 0
        while head!=None:# Basically, this method checks if the index that needs to be deleted is the next one from the current index.
                        #If true, it sets the current index's pointer to the 2nd element after it, thereby effectively cutting out the index that needs to be deleted from the list
             if count + 1 == index:
                 head.next = head.next.next
                 return
             count+=1
             head = head.next
        raise Exception('Out of Bounds')
            
# items = LinkedList()
# items.appendItems('PHP')
# items.appendItems('Python')
# items.appendItems('C#')
# items.appendItems('C++')
# items.appendItems('Java')
# items.printElements()
# items.findSize()
# items.findItem('Rahul')
# items.retItemAtIndex(2)
# items.setVal(1,2)
# items.printElements()
# items.delItems(1)
# items.printElements()
# items.delItems(0)
# items.printElements()





#====================================================================================================|
#Doubly Linked Lists                                                                                 
#Useful when you want to look at both previous and next elements                                     
#As a result, each node will have 2 pointers, and will have 3 attributes in total                    
#Pros:                                                                                               
    #1) DLL can be traversed in both forward and backward direction.
    #2) Deletion is quicker if you are given the node that has to be deleted, as you can use .prev pointers                                         
#Cons:                                                                                               
    #1) Since there are 2 pointers for each node, more space is required
    #2) There are more nodes to assign when deleting/inserting values
#====================================================================================================|
class Node2D(object):
    def __init__(self, value): #Attributes for each node, each node has a value and a pointer to the next node
        self.val = value
        self.next = None
        self.prev = None #We added the prev attribute to allow users to traverse both forward/backward over the array
                         #This will allow coders to look at elements before the current one, as well as after
        
class LinkedList(object):
    def __init__(self, head=None): #Initializes linked list
        self.head = head
        self.count = 0

    def appendElements(self, data):
        node = Node2D(data)
        if self.head: #If there is a head
            pointer = self.head #set the iterator to the head
            while pointer!=None: #scan the linked list till you reach the end
                lastElement = pointer
                pointer = pointer.next
            lastElement.next = node #you want to set the last element's next pointer to the new node
            node.prev = lastElement #Remember to set the previous pointer for the new node to the last Element because its a doubly linked list
            self.count+=1 #increment size of linked list by 1
        else:
            self.head = node #if there is no head, set the new node as the head. Then set the prev pointer to None, since its the first element.
            self.head.prev = None
            self.count+=1 #increment size of linked list by 1

    
    def delNode(self, index):
        pointer = self.head
        pos = 0
        if index == 0:  #If you want to delete the head, set the new head to the element after the original one
                        #set the prev pointer to None, and decrement the size of the list.
            self.head = self.head.next
            self.head.prev = None
            self.count-=1
            return
        elif index == self.count-1: #since I am deleting the last element, I need to do self.count - 1
            while pointer!= None:
                if pos == index: #when you reach the last position, set the previous element's next pointer to None(which effectively makes it the new tail)
                    pointer.prev.next = None 
                    self.count-=1 #decrement the size
                    return
                pointer = pointer.next
                pos+=1
        else: #This case is when you want to delete elements in the middle of the list
            while pointer!= None: 
                if pos == index: #Basically, you want to set the previous element's next pointer to the next element that comes after the current element(that will be deleted)
                                 #Also, you want to set the next element's(the one after the current element that will be deleted) previous pointer to the element before the current one
                                 #Since you effectively eliminated the pointer from the previous element to the current element, as well as the pointer from the current element to its previous/next, it will effectively be deleted


                    pointer.prev.next = pointer.next
                    pointer.next.prev = pointer.prev
                    self.count-=1 #decrement the count
                    return
                pointer = pointer.next
                pos+=1



    def insertNode(self, index, value):
        newNode = Node2D(value)
        pointer = self.head
        pos = 0
        if index == 0: #If inserting element at new head
            tmpVar = pointer.next
            tmpVar.prev=newNode
            newNode.next=tmpVar
            newNode.prev = None
            self.count+=1 #increment the size of the list
            return
        elif index == self.count: #If inserting element at the end of the list
            while pointer!= None:
                if pointer.next == None: #when you reach the last element, store it in a temporary variable
                    lastElement = pointer
                    break
                pointer = pointer.next
            lastElement.next = newNode #set the next element from the last to the new node(becomes the new tail)
            newNode.prev = lastElement #set the prev pointer for the new tail to the original tail
            newNode.next = None
            self.count+=1#increment the size of the list
            return
        else: #inserting the element somewhere in the middle of the list
            while pointer!= None:
                if pos == index:
                                #The explanation here may be complicated, so bear with me
                    prevElem = pointer.prev #set the element before the current one in a temporary veriable
                    pointer.prev = newNode #set the previous variable as the new one that needs to be inserted
                    newNode.next = pointer #the new node's next pointer must point to the current element
                    newNode.prev = prevElem #the new node's previous pointer must point to the prevElem variable(which contains the original previous element)
                    prevElem.next = newNode#set the original previous variable's next pointer to the new node
                    self.count+=1#increment the size
                    return 
                pos+=1
                pointer = pointer.next


    def printElements(self): #Prints linked list
        node = self.head
        res = ""
        while node != None:
            if node.next == None:
                res+=node.val
                break
            res+=(f"{node.val} --> ")
            node = node.next
        print(res)

items = LinkedList()
items.appendElements('PHP')
items.appendElements('Python')
items.appendElements('C#')
items.appendElements('C++')
items.appendElements('Java')
items.printElements()
items.delNode(2)
items.printElements()
print(items.count)
items.insertNode(4,"JavaScript")
items.printElements()
print(items.count)
items.insertNode(2, "HTML")
items.printElements()
print(items.count)
items.delNode(5)
items.printElements()
print(items.count)




#==========================================================
#
#                       Linked List Practice
#
#==========================================================


#Singly linked list
class Node():
    def __init__(self, value):
        self.val = value
        self.next = None

class LinkedList():
    def __init__(self, head):
        self.head = head

    def append(self, val):
        newNode = Node(val)
        if self.head == None:
            self.head = newNode
        else:
            elem = self.head
            while elem.next != None:
                elem = elem.next
            elem.next = newNode
            
    def findSize(self):
        if self.head:
            elem = self.head
            count = 0
            while elem != None:
                count+=1
                elem = elem.next
            print(count)
        else:
            print("Please enter values for the linked list, no values have been entered so far")

    def findElem(self, value):
        if self.head:
            elem = self.head
            while elem != None
                if elem.val   == value:
                    return True
                elem = elem.next
        return False

    def findItemAtIndex(self, index):
        pos = 0
        if self.head:
            elem = self.head
            while elem!=None:
                if pos == index:
                    return elem.val
                pos+=1
                elem = elem.next
        return Exception('Out of bounds/Linked lists isn\'t initialized yet')

    def setVal(self, index,value):
        pos = 0
        if self.head:
            elem = self.head
            while elem!=None:
                if pos == index:
                    elem.val = value
                pos+=1
                elem = elem.next
        return Exception('Out of bounds/Linked lists isn\'t initialized yet')
                







#Double Linked lists
class Node():
    def __init__(self, value):
        self.val = value
        self.next = None
        self.prev = None
        
class LinkedLists():
    def __init__(self, head):
        self.head = head
     #Takes care of adding an element to end of linked list, or if there is no linked list, creates the new head   
    def append(self, value):
        newNode = Node(value)
        if self.head:
            elem = newNode
            while elem.next != None:
                elem = elem.next
            lastElem = elem
            lastElem.next = newNode
            newNode.prev = lastElem
        else:
            self.head = newNode
            newNode.prev = None

    def sizeOfList(self):
        if self.head:
            elem = self.head
            count = 0
            while elem != None:
                count+=1
                elem = elem.next
            return count
        return 0
    
     #assumes head is already created       
    def insert(self, index, value):
        pos = 0
        newNode = Node(value)
        if index == 0:
            newNode.next = self.head
            newNode.prev = None
            self.head.prev = newNode
            self.head = newNode
        else:
            elem = self.head
            while elem != None:
                if pos == index:
                    prevElem = elem.prev
                    newNode.next = elem
                    elem.prev = newNode
                    newNode.prev = prevElem
                    prevElem.next = newNode
                pos+=1
                elem = elem.next
                return
        
            
        
            




















