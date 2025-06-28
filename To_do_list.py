import json
file_name = "tasks.json"
def read_tasks():
    try:
        f = open(file_name, "r")
        data = json.load(f)
        f.close()
        return data
    except:
        return []
def write_tasks(things):
    f = open(file_name, "w")
    json.dump(things, f)
    f.close()
def show(things):
    if len(things) == 0:
        print(" No tasks right now!")
    else:
        for i in range(len(things)):
            print(str(i + 1) + ". " + things[i])
def add(things):
    new = input("Write a new task: ")
    if new != "":
        things.append(new)
        write_tasks(things)
        print(" Task added!")
def remove(things):
    show(things)
    try:
        number = input("Type the number of the task to delete: ")
        index = int(number) - 1
        if index >= 0 and index < len(things):
            gone = things.pop(index)
            write_tasks(things)
            print(" Removed:", gone)
        else:
            print(" That number doesn't work.")
    except:
        print(" Please type a number.")
def main():
    things = read_tasks()

    while True:
        print("\n MENU")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        pick = input("Choose (1-4): ")
        if pick == "1":
            show(things)
        elif pick == "2":
            add(things)
        elif pick == "3":
            remove(things)
        elif pick == "4":
            print("CLOSING...")
            break
        else:
            print(" Please choose from 1 to 4.")
if __name__ == "__main__":
    main()
