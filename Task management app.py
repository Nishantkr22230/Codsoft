def task():
    tasks = [] #empty list
    print("------Welcome to the Task Management App-----")

    total_task = int(input("Enter how many task you want to enter = "))
    for i in range(1,total_task+1):
        task_name = input(f"Enter task {i} =")
        tasks.append(task_name)

    print(f"Today's task are\n{tasks}")


    while True:
        Operation = int(input("Enter 1-Add\n2-Update\n3-Delete\n4-View\n5-Exit|Stop"))
        if Operation == 1:
            add = input("Enter task yo want to add = ")
            tasks.append(add)
            print(f"Task {add} has been successfully added....")

        elif Operation == 2:
            update_val = input("Enter task number you want to update = ")
            if update_val in tasks:
                up = input("Enter new task = ")
                ind = tasks.index(update_val)
                tasks[ind] = up
                print(f"updated Task {up}")

        elif Operation == 3:
            del_val = input("Which task you want to delete = ")
            if del_val in tasks:
                ind = tasks.index( del_val)
                del tasks[ind]  
                print(f"Task {del_val} has been deleted....")
        elif Operation == 4:
            print(f" Total tasks = {tasks}")

        elif Operation == 5:
            print("closing the program..") 
            break

        else:
            print("Invalid operation")
              
task()