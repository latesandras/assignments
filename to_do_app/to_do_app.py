import sys

my_list = [] 
mark_list = []

my_file = open("textfile.txt", "r")

for line in my_file:
    my_list.append(line.split(",")[0])
    mark_list.append(line.split(",")[1].strip("\n"))   
my_file.close()

while True:
    command = input("Please specify a command [list, add, mark, archive]: ")

    if command == "add":
        item = input("Add an item: ")   
        my_list.append(item)
        mark_list.append("False")
        print("Item added.")

    elif command == "list":
        print("You saved the following to-do items: ")  
        i = 0
        for line in my_list:  
            if  mark_list[i] == "False":
                print("{}. [ ]".format(i + 1), line.strip())     
            else:
                print("{}. [x]".format(i + 1), line.strip())  
            i += 1

    elif command == "mark":
        print("You saved the following to-do items: ")  
        i = 0
        for line in my_list:  
            if  mark_list[i] == "False":
                print("{}. [ ]".format(i + 1), line.strip())     
            else:
                print("{}. [x]".format(i + 1), line.strip())  
            i += 1
        linemark = int(input("Which one you want to mark as completed: ")) 
        mark_list[linemark-1] = "True"      
        print("{} is completed" .format(my_list[linemark-1].strip("\n")))   

    elif command == "archive":
        i = 0
        while i < len(mark_list):
            if mark_list[i] == "True":
                del(mark_list[i])
                del(my_list[i])
            else:
                i += 1
        print("All completed tasks got deleted.")

    elif command == "x":
        my_file = open("textfile.txt", "w")
        i=0
        for line in my_list:
            my_file.write(line +"," + mark_list[i] + "\n")
            i += 1
        my_file.close()
        print(my_list)
        print(mark_list)
        sys.exit()