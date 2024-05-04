class Employee:

    def __init__(self, ssn, name, dept, designation, sal, phno):
        self.ssn = ssn
        self.name = name
        self.dept = dept
        self.designation = designation
        self.sal = sal
        self.phno = phno

class Node:
    
    def __init__(self, employee):
        self.employee = employee
        self.next = None
        self.prev = None

class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def insert_at_end(self, employee):
        new_node = Node(employee)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node 
        self.count += 1
        print("Employee info inserted at the end!")