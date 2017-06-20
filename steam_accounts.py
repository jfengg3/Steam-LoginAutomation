import sys, json, os

try:
    with open('accounts.data', 'r') as d:
        accountlist = json.load(d)
    d.close()
except FileNotFoundError:
    with open('accounts.data', 'w') as f:
        accountlist = {}
        json.dump(accountlist,f)
    f.close()

def menu():
    opt1, opt2, opt3, opt4, opt5 = "\n1. Accounts list", "\n2. Add account", "\n3. Remove account", "\n4. Edit account", "\n5. Exit"
    print("==[Steam Accounts]=="+opt1+opt2+opt3+opt4+opt5)

def active():
    opt1, opt2 = "\n1. Change account activity: ", "\n2. Back"
    print(opt1+opt2)

def addaccount():
    uid = input("Enter an unique id: ")
    if uid in accountlist:
        print("\nUid already existed!")
    else:
        adduser = input("Account username: ")
        addpass = input("Account password: ")

        accountlist[uid] = [adduser, addpass, '0']
        print("\nAccount added successfully!")

def editmenu():
    opt1, opt2 = "\n1. Change password", "\n2. Back"
    print("==[Edit Account]=="+opt1+opt2+opt3)

def start():
    running = True

    while (running):
        menu()
        try:
            choice = int(input("\nOption: "))
        except ValueError:
            print("Only integers are allowed.")
            continue

        if choice == 1:

            if len(accountlist) >= 1:
                display = "[UID]\t\t[Account Id]\t[Password]\t[Active]\n"
                row = ""
                for uid in accountlist:
                    row += uid+"\t\t"+accountlist[uid][0]+"\t"+accountlist[uid][1]+"\t"+accountlist[uid][2]+"\n"
                print(display + row)

                activemenu = True
                while (activemenu):
                    active()
                    try:
                        choice = int(input("\nOption: "))
                    except ValueError:
                        print("Only integers are allowed.")
                        continue

                    if choice == 1:

                        uid = input("Enter the unique id to set activity: ")
                        if uid in accountlist:

                            if accountlist[uid][2] == '1':
                                accountlist[uid][2] = '0'
                                print(uid + " is set to inactive.")
                                count = 0
                                for account in accountlist:
                                    if accountlist[account][2] == '0':
                                        count += 1
                                if count == len(accountlist):
                                    os.remove('login.data')
                                count = 0

                            elif accountlist[uid][2] == '0':
                                count = 0
                                for account in accountlist:
                                    if accountlist[account][2] == '1':
                                        count += 1
                                if count >= 1:
                                    print("There can be only 1 active account at a time!")
                                else:
                                    accountlist[uid][2] = '1'
                                    #Get username, password if active & save it
                                    with open('login.data', 'w') as f:
                                        credentials = [uid,accountlist[uid][0], accountlist[uid][1]]
                                        json.dump(credentials,f)
                                    f.close()
                                    print(uid + " is set to active.")
                                count = 0

                        else:
                            print("\nUid does not exist in database!")

                    elif choice == 2:
                        activemenu = False

                    else:
                        print("Invalid choice")

            else:
                print("\nThere are no accounts yet. ")
                prompt = input("Would you like to add one? (Y/N)")

                if prompt.lower() == 'y':
                    addaccount()
                else:
                    print("It's fine!")

        elif choice == 2:

            addaccount()

        elif choice == 3:

            uid = input("Enter the unique id for deletion: ")
            if uid in accountlist:
                del accountlist[uid]
                print("\n"+ uid + " has been removed.")
                count = 0
                for account in accountlist:
                    if accountlist[account][2] == '0':
                        count += 1
                if count == len(accountlist):
                    os.remove('login.data')
                count = 0
            else:
                print("\nUid does not exist in database!")

        elif choice == 4:

            uid = input("Enter the unique id for edition: ")
            if uid in accountlist:
                submenu = True
                while (submenu):
                    editmenu()
                    try:
                        choice = int(input("\nOption: "))
                    except ValueError:
                        print("Only integers are allowed.")
                        continue

                    if choice == 1:
                        cpass = input("Change password to?: ")
                        accountlist[uid][1] = cpass
                        print("\nPassword has been changed!")

                    elif choice == 2:
                        submenu = False

                    else:
                        print("Invalid choice")

            else:
                print("\nUid does not exist in database!")

        elif choice == 5:
            running = False

            print("Program exited.")
            with open('accounts.data', 'w') as f:
                json.dump(accountlist,f)
            f.close()

            sys.exit(0)

        else:
            print("Invalid choice.")

if __name__ == "__main__":
   start()
