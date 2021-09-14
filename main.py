def getdate():
    import datetime
    return datetime.datetime.now()
try:
    def take(k):
        if (k==1):
            c = int(input("Enter 1 for excersise and 2 for food -> "))
            if(c==1):
                value = input("Type Here: \n")
                with open("StoreGet/larry-excer.txt","a") as f:
                    f.write(str([str(getdate())]) + ":" + value + "\n")
                print("Written Sucessfuly")
            elif(c==2):
                value = input("Type Here: \n")
                with open("StoreGet/larry-food.txt","a") as f:
                    f.write(str([str(getdate())]) + ":" + value + "\n")
                print("Written Sucessfuly")
        elif(k==2):
            c = int(input("Enter 1 for excersise and 2 for food -> "))
            if(c==1):
                value = input("Type Here: \n")
                with open("StoreGet/rohan-excer.txt","a") as f:
                    f.write(str([str(getdate())]) + ":" + value + "\n")
                print("Written Sucessfuly")
            elif(c==2):
                value = input("Type Here: \n")
                with open("StoreGet/rohan-food.txt","a") as f:
                    f.write(str([str(getdate())]) + ":" + value + "\n")
                print("Written Sucessfuly")
        elif(k==3):
            c = int(input("Enter 1 for excersise and 2 for food -> "))
            if(c==1):
                value = input("Type Here: \n")
                with open("StoreGet/sohan-excer.txt","a") as f:
                    f.write(str([str(getdate())]) + ":" + value + "\n")
                print("Written Sucessfuly")
            elif(c==2):
                value = input("Type Here: \n")
                with open("StoreGet/sohan-food.txt","a") as f:
                    f.write(str([str(getdate())]) + ":" + value + "\n")
                print("Written Sucessfuly")
    def view(k):
        if (k==1):
            c = int(input("Enter 1 for excersise and 2 for food -> "))
            if(c==1):
                with open("StoreGet/larry-excer.txt","r") as f:
                    for i in f:
                        print(i,end="")
            elif(c==2):
                with open("StoreGet/larry-food.txt","r") as f:
                    for i in f:
                        print(i,end="")
        elif(k==2):
            c = int(input("Enter 1 for excersise and 2 for food -> "))
            if(c==1):
                with open("StoreGet/rohan-excer.txt","r") as f:
                    for i in f:
                        print(i,end="")
            elif(c==2):
                with open("StoreGet/rohan-food.txt","r") as f:
                    for i in f:
                        print(i,end="")
        elif(k==3):
            c = int(input("Enter 1 for excersise and 2 for food -> "))
            if(c==1):
                with open("StoreGet/sohan-excer.txt","r") as f:
                    for i in f:
                        print(i,end="")
            elif(c==2):
                with open("StoreGet/sohan-food.txt","r") as f:
                    for i in f:
                        print(i,end="")
    print("-----------------------------------------------------------------")
    print("Welcome to Taqatwar Gym Center |Track Your Gym Practise and Gym Diet|")
    print("-----------------------------------------------------------------")
    a = int(input("Press 1 for Log and 2 for retrieve -> "))
    if(a==1):
        b = int(input("Press |1 for larry, 2 for Rohan, 3 for Sohan| -> "))
        take(b)
    else:
        b = int(input("Press |1 for larry, 2 for Rohan, 3 for Sohan|-> "))
        view(b)
except Exception as e:
    print("Invalid Input")