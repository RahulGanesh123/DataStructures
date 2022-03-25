#=============================
#Stacks:
# 1) Basically a data structure that is a linear collection of items
# 2) You can't access random elements like you can in a list, but you can delete and insert elements extremely quickly
# 3) LIFO -- Last in 1st out. Basically means that a stack is built using push() and pop() operations. Insertion + Deletion happen on the same end, as opposed to normal lists.
# 4) Push  -- adding an elment to the top of the stack. Pop -- returning an element that is the top of the stack + deleting it
# 5) Pros:
#   a)Insert and delete operations always happen in O(1) -- which means that they always occur in the same amount of time, regardless of the size of the stack, because you only insert/delete at the end of the stack, so it will always take constant time
#       whereas, in arrays/lists, insertions and deletions would take O(n) because insertions/deletions require extra memory as the computer needs to allocate new memory to the array and shift the array over
#
#
#
#
#=============================


class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self,val):
        self.stack.append(val)
        
    def pop(self):
        return self.stack.pop() #pop() is a built in method to Python. It returns the top element of the stack as well as deletes it from the stack
    
    def peek(self):
        return  self.stack[-1]
    
    def is_empty(self):
        return size() == 0
    
    def size(self):
        return len(self.stack)

    def get_stack(self):
        print(self.stack)


#To understand stacks better, think of back buttons on websites
#Whenever you click the back button, you pop the top element off a stack and the element before it becomes the next top
#You keep getting redirected until you reach the 1st webpage u used, where u see a greyed back button. It doesn't allow you to go back even further because popping the stack would result in an empty stack.

#[2,3,4,5]
# stack.pop() --> 5 and its removed from the stack
# stack.push(6) --> stack becomes [2,3,4,5,6]
#notice that everything happens at the end of the stack. That is, both insertions/deletions happen toward the end of the stack



#------------
#         3         | => (The top of the stack. This is what gets popped, and this is the only value in the stack that the user can view.)
#------------
#          2        |
#------------
#          1        |
#------------

#This is a visual representation of a stack. Let's go over some real-life examples of how stacks are used:
        #Website back button:
                    #-------------------------------------------
                    #         www.cnn/global/india/bangalore         | => (The top of the stack. This is what gets popped, and this is the only value in the stack that the user can view.)
                    #-------------------------------------------
                    #          www.cnn/global/india                           |
                    #-------------------------------------------
                    #          www.cnn/global                                    |
                    #-------------------------------------------
                    #          www.cnn                                                |
                    #-------------------------------------------

        #Click back-button one time
                    #This means that the stack will conduct a push operation, which means the last link, the one with bangalore, would be removed from the stack and that the new end of the stack would be the /india
                    #You would be redirected to the india page of cnn's global website
                    #The stack would now look like this:
                            #-------------------------------------------
                            #          www.cnn/global/india                           | => This is the new top of the stack
                            #-------------------------------------------
                            #          www.cnn/global                                    |
                            #-------------------------------------------
                            #          www.cnn                                                |
                            #-------------------------------------------






class Queue:
    def __init__(self):
        self.queue = []
    
    def push(self,val):
        self.queue.append(val)
        
    def pop(self):
        return self.queue.pop(0) 
    
    def peek(self):
        return  self.queue[0]
    
    def is_empty(self):
        return size() == 0
    
    def size(self):
        return len(self.queue)

    def get_queue(self):
        print(self.queue)


# Queues are basically stacks, but instead of LIFO behavior, its FIFO. That is, The first element gets deleted, not the last one. However, elements are still added at the end of the queue

#Examples of basic queue operations:
# [2,3,4,5]
# queue.pop() --> 2 is removed from the beginning of the queue, and the stack is now => [3,4,5]
# queue.push(2) --> 2 is added to the beginning of the queue, and the stack is now [3,4,5,2]


#Think of queues as lines of people waiting to get food. People have to join the line at the end, but leave the line at the beginning.
#A good way to understand the difference between stacks and queues is that in stacks, you delete the most recent item that was added to the stack, but in the queue, you remove the item that was added the least recently


#This is a visual representation of a stack. Let's go over some real-life examples of how stacks are used:
        #Line for food:
                    #-------------------------------------------
                    #                       Bob                                               | => (The top of the queue. This is what gets popped, and this is the only value in the stack that the user can view.)
                    #-------------------------------------------
                    #                      John                                              |
                    #-------------------------------------------
                    #                      Jackie                                           |
                    #-------------------------------------------
                    #                       Ben                                              |
                    #-------------------------------------------

        #Rahul joins the line
                    #This means that the queue will conduct a push operation, which means that Rahul would join the queue at its end(remember stacks and queues share the same push operation, they just differ in the deletion)
                    #The queue would now look like this:
                    #-------------------------------------------
                    #                       Bob                                               | => (The queue of the stack. This is what gets popped, and this is the only value in the stack that the user can view.)
                    #-------------------------------------------
                    #                      John                                              |
                    #-------------------------------------------
                    #                      Jackie                                           |
                    #-------------------------------------------
                    #                       Ben                                              |
                    #-------------------------------------------
                    #                       Rahul                                           |
                    #-------------------------------------------

       #Bob gets his food
                    #This means that the queue will conduct a pop operation, which means that Bob would leave the queue at its front

                    #The queue would now look like this:
                    #-------------------------------------------
                    #                      John                                              | => The new top of the queue
                    #-------------------------------------------
                    #                      Jackie                                           |
                    #-------------------------------------------
                    #                       Ben                                              |
                    #-------------------------------------------
                    #                       Rahul                                           |
                    #-------------------------------------------



























#Some Pros of Stacks/Queues:
# a) Some great benefits is that insertions and deletions for stacks and queues take O(1) time as all insertions and deletions happen at the beginning/end of the queue/stack
#   i) Normal Lists would take O(n) as insertions/deletions depend on the size of the array, as both will have to shift elements in the array, which takes extra runtime/memory
