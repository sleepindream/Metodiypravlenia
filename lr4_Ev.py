user_ids=["Evgeniy","Pavel","Alexey","Semen","Andrey","Denis","Sasha"]
files=["Object 1","Object 2","Object 3","Object 4"]
access_name=["Complete ban","Broadcast right","Write","Write & Broadcast right","Read","Read & Broadcast right","Write & Read","Complete access"]
files_access=[[7,7,7,7],[7,1,0,2],[0,0,0,4],[2,3,3,5],[7,0,0,0],[1,2,3,4],[4,3,2,1]]
def logIn(user_id):
    if (user_id in user_ids):
        print("Identification was successful, welcome to the system!")
        printRights(user_id)
        return True
    print("Invalid Login")
    return False
def brodcastRight(user_id,file_id):
    new_user=input("Input user id : \n")
    files_access[user_ids.index(new_user)][file_id]=files_access[user_ids.index(user_id)][file_id]
    print("Complited...")
def printRights(user_id):
    for i in range(len(files)):
        print(files[i]+' - '+ access_name[files_access[user_ids.index(user_id)][i]])
def checkRight(user_id,right):
    file=int(input("Input file id : \n"))
    if right=="w":
        if (files_access[user_ids.index(user_id)][file-1]==2) or (files_access[user_ids.index(user_id)][file-1]==3) or (files_access[user_ids.index(user_id)][file-1]==6) or (files_access[user_ids.index(user_id)][file-1]==7):
            print("Allow access")
            return True
    if right=="r":
        if files_access[user_ids.index(user_id)][file-1]==4 or files_access[user_ids.index(user_id)][file-1]==5 or files_access[user_ids.index(user_id)][file-1]==6 or files_access[user_ids.index(user_id)][file-1]==7:
            print("Allow access")
            return True
    if right=="g":
        if files_access[user_ids.index(user_id)][file-1]==1 or files_access[user_ids.index(user_id)][file-1]==3 or files_access[user_ids.index(user_id)][file-1]==5 or files_access[user_ids.index(user_id)][file-1]==7:
            print("Allow access")
            brodcastRight(user_id,file-1)
            return True
    print("Access denied")
command=""
current_user=None
current_obj=None
while(command!="cl"):
    if (current_user==None):
        id=input("Enter user id : \n")
        if logIn(id):
            current_user=id
        else:
            continue
    command=input("Enter command : \n")
    if command=="w":
        checkRight(current_user,"w")
    if command=="r":
        checkRight(current_user,"r")
    if command=="g":
        checkRight(current_user,"g")
