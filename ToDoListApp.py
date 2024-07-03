todo_list = []

def addList():
    item = input("Enter a new Task: ")
    todo_list.append(item)
    print(f"{item} added to the todo list")

def displayList():
    print("----------")
    print("Todo List")
    print("----------")
    for index, item in enumerate(todo_list, start=1):
        print(f"{index} - {item}")

def removeList():
    displayList()
    index = int(input("Enter your item to remove: "))-1
    if 0 <= index < len(todo_list):
         removed_item = todo_list.pop(index)
         print(f"{removed_item} removed from the todo list")

    else:
        print("Invalid input.....!")




while True:
    print("##################")
    print("To Do List App")
    print("##################")
    print("1. Add To List")
    print("2. Display List")
    print("3. Remove from List")
    print("4. Exit")


    option = input("Select your Option: ")

    if option == '1':
        addList()

    if option == '2':
        displayList()

    if option == '3':
        removeList()

    if option == '4':
        print("Exit")
        break

    else:
        print("Invalid option.....!")