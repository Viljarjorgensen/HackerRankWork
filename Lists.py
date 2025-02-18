global list
global OutPutList

def Insert(index, integer):
    list.insert(int(index), int(integer))

def PrintList():
    OutPutList.append(list.copy())

def Remove(integer):
    list.remove(int(integer))

def Append(integer):
    list.append(int(integer))

def Sort():
    list.sort()

def Pop():
    list.pop()

def Reverse():
    list.reverse()

if __name__ == '__main__':
    list = []
    OutPutList = []
    N = int(input())

    for i in range(N):
        choice = input().strip().split()
        command = choice[0]

        if command == "insert":
            Insert(int(choice[1]), int(choice[2]))
        elif command == "print":
            PrintList()
        elif command == "append":
            Append(int(choice[1]))
        elif command == "remove":
            Remove(int(choice[1]))
        elif command == "pop":
            Pop()
        elif command == "sort":
            Sort()
        elif command == "reverse":
            Reverse()

    for snapshot in OutPutList:
        print(snapshot)
