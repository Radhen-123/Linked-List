class LinkedListNode:                                   #Defininng Structure of LinkedList
    def __init__(self, Data, NextNode = None):
        self.Data = Data                                #Data Portion
        self.NextNode = NextNode                        #Address Portion

class LinkedList:
    def __init__(self, Start = None):
        self.Start = Start                              #Start Will always point To First Element
                                                        #All Functions Performed by Linked List

    def Insert_At_Start(self, Data):
        NewNode = LinkedListNode(Data)
        NewNode.NextNode = self.Start
        self.Start = NewNode


    def Insert_At_End(self, Data):
        NewNode = LinkedListNode(Data)
        Pointer = self.Start
        if  Pointer == None:
            self.Insert_At_Start(Data)
        else:
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

    def Insert_Before_Number(self, Number, Data):
        Pointer = self.Start
        NewNode = LinkedListNode(Data)
        Count = 0
        if Number ==   Pointer.Data:
            self.Insert_At_Start(Data)
        else:
            while Pointer.Data != Number and Pointer.NextNode != None:
                PrePointer = Pointer
                Pointer = Pointer.NextNode
                Count += 1
            PrePointer.NextNode = NewNode
            NewNode.NextNode = Pointer


    def Insert_After_Number(self, Number, Data):
        Pointer = self.Start
        PastPointer = Pointer.NextNode
        NewNode = LinkedListNode(Data)
        while Pointer.Data != Number and Pointer.NextNode != None:
            Pointer = Pointer.NextNode
            PastPointer =PastPointer.NextNode
        Pointer.NextNode = NewNode
        NewNode.NextNode = PastPointer

    def Delete_At_Start(self):
        Pointer = self.Start
        if Pointer == None:
            print("List is Empty")
            return None
        else:
            self.Start = Pointer.NextNode
            del Pointer


    def Delete_At_End(self):
        Pointer = self.Start
        if Pointer == None:
            print("List is Empty")
            return None
        else:
            while Pointer.NextNode != None:
                PrePointer = Pointer
                Pointer = Pointer.NextNode
            PrePointer.NextNode = None
            del Pointer

    def Delete_At_Index(self, Index):
        FindIndex = 1
        Pointer = self.Start
        if Pointer == None:
            print("List is Empty")
            return None
        elif Index <= 0:
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

    def Delete_Number(self, Number):
        Pointer = self.Start
        if Pointer == None:
            print("List is Empty")
        else:
            while Pointer.Data != Number:
                PrePointer = Pointer
                Pointer = Pointer.NextNode
            PrePointer.NextNode = Pointer.NextNode
            del Pointer
    def Print_Linked_List(self):
        Begin = self.Start
        Count = 0
        if Begin == None:
            print("No Data To print")
        else:
            while Begin != None:
                Count += 1
                print("Index:" + str(Count) + " Data: " + str(Begin.Data))
                Begin = Begin.NextNode

    def Length(self):
        Count = 0
        StartPointer = self.Start
        while StartPointer != None:
            StartPointer = StartPointer.NextNode
            Count += 1
        return Count

def Function_Of_Linked_List():
    print("*********Index Menu**********")
    print("1 For insert Data at Start")
    print("2 For insert Data at End")
    print("3 For insert Data at Index")
    print("4 For insert Data Before Number")
    print("5 For insert Data after Number")
    print("6 For Delete Element at Start")
    print("7 For Delete Element at End")
    print("8 For Delete Element at Index")
    print("9 For Delete given Number")
    print("10 Print Length of list")
    print("11 for exit")
    Linked_List = LinkedList()
    Start = 0
    while Start != 11:
        Number = int(input("Enter your Selection: "))
        if Number == 1:
            Data = int(input("Enter Data to insert: "))
            Linked_List.Insert_At_Start(Data)
            Linked_List.Print_Linked_List()
        elif Number == 2:
            Data = int(input("Enter Data to insert: "))
            Linked_List.Insert_At_End(Data)
            Linked_List.Print_Linked_List()
        elif Number == 3:
            Data = int(input("Enter Data to insert: "))
            Index = int(input("Enter Index: "))
            Linked_List.Insert_At_Index(Index, Data)
            Linked_List.Print_Linked_List()
        elif Number == 4:
            Data = int(input("Enter Data to insert: "))
            BeforeNumber = int(input("Before which Number: "))
            Linked_List.Insert_Before_Number(BeforeNumber, Data)
            Linked_List.Print_Linked_List()
        elif Number == 5:
            Data = int(input("Enter Data to insert: "))
            AfterNumber = int(input("After which Number: "))
            Linked_List.Insert_After_Number(AfterNumber, Data)
            Linked_List.Print_Linked_List()
        elif Number == 6:
            Linked_List.Delete_At_Start()
            Linked_List.Print_Linked_List()
        elif Number == 7:
            Linked_List.Delete_At_End()
            Linked_List.Print_Linked_List()
        elif Number == 8:
            Index = int(input("Enter Index: "))
            Linked_List.Delete_At_Index(Index)
            Linked_List.Print_Linked_List()
        elif Number == 9:
            Number = int(input("Enter Number To Delete: "))
            Linked_List.Delete_Number(Number)
            Linked_List.Print_Linked_List()
        elif Number == 10:
            print(Linked_List.Length())
        Start = Number
Function_Of_Linked_List()
