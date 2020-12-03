import os
import json
usr_dir = dict()
web_data = dict()
id_pass = dict()
fh = os.path.abspath('D:\\Python\\Projects\\Passman.txt')
ah = os.path.abspath('D:\\Python\\Projects\\MainLogin.txt')
if os.path.exists(fh):
    auth = open(ah , 'r+')
    store = open(fh , 'r+')
else:
    auth = open(ah , 'w+')
    store = open(fh , 'w+')
dh = store.read()
eh = auth.read()
if (dh):
    usr_dir = json.loads(dh)
if (eh):
    id_pass = json.loads(eh)
while True:
    print("*"*50+"\n")
    print("Select A Number From The Following:\n")
    print("1.Create A New User\n")
    print("2.Open An Existitng User Record\n")
    print("3.Exit\n")
    print("*"*50+"\n")
    initnum = int(input())
    if initnum == 2:
        usr_name = input("Enter Username\n")
        if usr_name in id_pass:
            print("Welcome Back "+str(usr_name)+"\n")
            print("Enter Your PassWord To Access:\n")
            passw = input("\n")
            if (id_pass[usr_name] == passw):
                print("Access Granted\n")
                while True:
                    print("*"*50+"\n")
                    print("Select A Number From The Following:\n")
                    print("1.Create A New Entry\n")
                    print("2.Print Existing Entries\n")
                    print("3.Go Back\n")
                    print("*"*50+"\n")
                    num = int(input("\n"))
                    if num == 1:
                        print("Enter The Webiste Name\n")
                        webname = input("\n")
                        if webname in usr_dir:
                            print("Website Already Exists\n")
                        else:
                            print("Enter The Username / Email As On "+str(webname))
                            tempname = input("\n")
                            print("Enter The Password For "+str(webname))
                            temppass = input("\n")
                            web_data[webname] = {tempname : temppass}
                            usr_dir[usr_name] = web_data
                    elif num == 2:
                        print(usr_dir[usr_name])
                    elif num == 3:
                        break
                    else:
                        print("Wrong Input")
            else:
                print("Wrong Password")
        else:
            print("User Doesn't Exist") 
    elif initnum == 1:
        usr_name = input("Enter UserName:\n")
        if usr_name in id_pass:
            print("User Already Exists.\n")
            print("Exiting...")
        else:
            print("Welcome "+str(usr_name)+"\n")
            print("Enter A Password to continue\n")
            passw = input("\n")
            id_pass[usr_name] = passw
    elif initnum == 3:
        print("Exiting...")
        break
    else:
        print("Wrong Input")
store.seek(0)
store.write(json.dumps(usr_dir))
store.truncate()
auth.seek(0)
auth.write(json.dumps(id_pass))
auth.truncate()
