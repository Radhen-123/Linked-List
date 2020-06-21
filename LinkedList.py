class LinkedListNode:
    def __init__(self, Data, NextNode = None):
        self.Data = Data
        self.NextNode = NextNode

class LinkedList:
    def __init__(self, Start = None):
        self.Start = Start

    def Insert_At_Start(self, Data):
        NewNode = LinkedListNode(Data)
        NewNode.NextNode = self.Start
        self.Start = NewNode

    def Insert_At_End(self, Data):
        NewNode = LinkedListNode(Data)
        Pointer = self.Start
        while Pointer.NextNode != None:
            Pointer = Pointer.NextNode
        Pointer.NextNode = NewNode
        
        
    def Insert_At_Index(self, Index, Data):
        NewNode = LinkedListNode(Data)
        FindPointer = 1
        if(Index <= 0):
            print("Insertion at Invalid Index")
        elif(Index == 1):
            self.Insert_At_Start(Data)
        elif (Index <= self.Length()):
            Pointer = self.Start
            while FindPointer != Index:
                PrePointer = Pointer
                Pointer = Pointer.NextNode
                FindPointer += 1
            PrePointer.NextNode = NewNode
            NewNode.NextNode = Pointer
        elif (Index == self.Length() + 1):
            self.Insert_At_End(Data)
        else:
            print("Insertion Out of Range")



    def Delete_At_Start(self):
        Pointer = self.Start
        self.Start = Pointer.NextNode
        del Pointer

    def Delete_At_End(self):
        Pointer = self.Start
        while Pointer.NextNode != None:
            PrePointer = Pointer
            Pointer = Pointer.NextNode
        PrePointer.NextNode = None
        del Pointer
        
    def Delete_At_Index(self, Index):
        FindIndex = 1
        Pointer = self.Start
        if Index <= 0:
            print("Deletion Invalid Index")
        elif (Index == 1):
            self.Delete_At_Start()
        elif(Index == self.Length()):
            self.Delete_At_End()
        elif Index <= self.Length() :
            while FindIndex != Index:
                PrePointer = Pointer
                Pointer = Pointer.NextNode
                FindIndex += 1
            PrePointer.NextNode = Pointer.NextNode
            del Pointer
        else:
            print("Deletion Out of Range")
        
        

    def Print_Linked_List(self):
        Begin = self.Start
        while Begin != None:
            print(Begin.Data)
            Begin = Begin.NextNode

ll = LinkedList()
ll.Insert_At_Start(685)
ll.Insert_At_Start(54)
ll.Insert_At_Start(79)
ll.Insert_At_End(65)
ll.Insert_At_End(56)
ll.Print_Linked_List()
print("Update")
ll.Delete_At_Start()
ll.Delete_At_End()
ll.Print_Linked_List()
