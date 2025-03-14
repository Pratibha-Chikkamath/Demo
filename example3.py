class Node:
    def _init_(self, data):
        self.data = data;
        self.next = None;


class CircularLinkedList:

    # Declaring Circular Linked List
    def _init_(self):
        self.head = Node(None);
        self.tail = Node(None);
        self.head.next = self.tail;
        self.tail.next = self.head;

        # Adds new nodes to the Circular Linked List

    def add(self, data):

        # Declares a new node to be added
        newNode = Node(data);

        # Checks if the Circular
        # Linked List is empty
        if self.head.data is None:

            # If list is empty then new node
            # will be the first node
            # to be added in the Circular Linked List
            self.head = newNode;
            self.tail = newNode;
            newNode.next = self.head;

        else:
            # If a node is already present then
            # tail of the last node will point to
            # new node
            self.tail.next = newNode;

            # New node will become new tail
            self.tail = newNode;

            # New Tail will point to the head
            self.tail.next = self.head;

            # Function to search the element in the

    # Circular Linked List
    def findNode(self, element):

        # Pointing the head to start the search
        current = self.head;
        i = 1;

        # Declaring f = 0
        f = 0;
        # Check if the list is empty or not
        if (self.head == None):
            print("Empty list");
        else:
            while (True):
                # Comparing the elements
                # of each node to the
                # element to be searched
                if (current.data == element):
                    # If the element is present
                    # then incrementing f
                    f += 1;
                    break;

                    # Jumping to next node
                current = current.next;
                i = i + 1;

                # If we reach the head
                # again then element is not
                # present in the list so
                # we will break the loop
                if (current == self.head):
                    break;

                    # Checking the value of f
            if (f > 0):
                print("element is present");
            else:
                print("element is not present");