#dynamic to-do list

tasks= []
while true:
    print("\n---- to do list----")
    print("1. add task")
    print("2. view task")
    print("3. remove task")
    print("4. exit")
    choice = input("enter your choice: ")
    if choice == "1":
        task = input("enter new task: ")
        tasks.append(task)
        print("task added successfully!")
    elif choice == "2":
        if len(tasks) == 0:
            print("no tasks in the list.")
        else:
            print("\nyour tasks:")
            for i in range(len(tasks)):
                print(i + 1, "-", tasks[i])
    elif choice == "3":
        if len(tasks) == 0:
            print("no tasks to remove.")
        else:
            for i in range(len(tasks)):
                print(i + 1, "-", tasks[i])
            num = int(input("enter task number to remove: "))
            if num > 0 and num <= len(tasks):
                removed = tasks.pop(num - 1)
                print(removed, "removed from list.")
            else:
                print("invalid task number.")
    elif choice == "4":
        print("exiting program...")
        break
    else:
        print("invalid choice! try again.")