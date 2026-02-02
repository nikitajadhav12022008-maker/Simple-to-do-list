Tasks = []

while True:
    print("1.Add 2.View 3.Remove 4.Exit")
    ch = int(input("choice:"))

    if(ch == 1):
        Tasks.append(input("tasks:"))
    elif(ch == 2):
        print(Tasks)
    elif(ch == 3):
        Tasks.remove(input("task to remove:"))
    elif(ch == 4):
        break