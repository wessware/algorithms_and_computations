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

    def insert_at_front(self, employee):
        new_node = Node(employee)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.count += 1
        print("Employee info inserted at the front!")
    
    def delete_at_end(self):
        if self.head is None:
            print("Doubly linked list has employee info to delete!")
        elif self.head == self.tail:
            self.head = None
            self.tail = None
            self.count -= 1
            print("Employee info deleted from the end!")
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            self.count -= 1
            print("Employee info deleted from the end!")

    def delete_from_front(self):
        if self.head is None:
            print("Doubly Linked list has no employee data!")
        elif self.head == self.tail:
            self.head = None
            self.tail = None
            self.count -= 1
        else:
            self.head = self.head.next
            self.head.prev = None
            self.count -= 1
            print("Employee info deleted from front!")

    def dll_display(self):
        if self.head is None:
            print("This DLL has not data!")
        else:
            current = self.head
            print("Doubly Linked List displaying!")

            while current:
                print("SSN: ", current.employee.ssn)
                print("NameL: ", current.employee.name)
                print("Department: ", current.employee.dept)
                print("Designation: ", current.employee.designation)
                print("Salary: ", current.employee.sal)
                print("Phone Number: ", current.employee.phno)
                print("------------")
                current = current.next
    def nodes_sum(self):
        print("This DLL has: " + self.count + " nodes")

dll = DoublyLinkedList()

while True:
    print("-------DLL Display------")
    print("OP1: Create a DLL of n employees with end insertion")
    print("OP2: Display DLL and count the number of nodes")
    print("OP3: Insertion at end operation")
    print("OP4: Insertion at front operation")
    print("OP5: Deletion at end operation")
    print("OP6: Deletion at front operation")
    print("OP7: DLL as double-end queue operation")
    print("OP8: Exit program")
    print("--------END----------")

    choice = input("Choose and operation from the list: ")

    if choice == "OP1":
        n = int(input("Provide the number of employees: "))
        for _ in range(n):
            ssn = input("SSN number: ")
            name = input("Employee name: ")
            dept = input("Employee department: ")
            designation = input("Employee designation: ")
            sal = input("Employee salary: ")
            phno = input("Employee phone number: ")

            emp = Employee(ssn, name, dept, designation, sal, phno)
            dll.insert_at_end(emp)
        dll.dll_display()
        dll.nodes_sum()

    if choice == "OP2":
        dll.dll_display()
        dll.nodes_sum()

    elif choice == "OP3":
        ssn = input("SSN Number: ")
        name = input("Employee name: ")
        dept = input("Employee department: ")
        designation = input("Employee designation: ")
        sal = float(input("Employee salary: "))
        phno = input("Employee phone number: ")

        employee = Employee(ssn, name, dept, designation, sal, phno)
        dll.insert_at_end(employee)
        dll.dll_display()
        dll.nodes_sum()

    elif choice == "OP4":
        ssn = input("SSN Number: ")
        name = input("Enter employee number: ")
        dept = input("Employee department" )
        designation = input("Employee designation: ")
        sal = float(input("Enter employee salary: "))
        phno = input("Enter employee phone number: ")

        employee = Employee(ssn, name, dept, designation, sal, phno)
        dll.insert_at_front(employee)
        dll.dll_display()
        dll.nodes_sum()

    elif choice == "OP5":
        dll.delete_at_end()
        dll.dll_display()
        dll.nodes_sum()

    elif choice == "OP6":
        dll.delete_from_front()
        dll.dll_display()
        dll.nodes_sum()

    elif choice == "OP7":
        while True:
            print("------Implementation as Double-Ended Queue")
            print("OP1_1: Insertion at end operation")
            print("OP2_2: Insert at front operation")
            print("OP3_3: Deletion at end operation")
            print("OP4_4: Deletion at front operation")
            print("OP5_5: Return to main application")
            print("--------END----------")

            sec_choice = input("Select a DE-Queue operation: ")

            if sec_choice == "OP1_1":
                ssn = 

