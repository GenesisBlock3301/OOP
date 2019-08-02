userNameList = list()
class UserRegistration:

    def __init__(self):
        pass

    def signup(self, username, password):
        for i in open('account.txt', 'r').readlines():
            if username == i.split(" ")[0]:
                userNameList.append(i.split(" ")[0])
        if username not in userNameList:
           file = open('account.txt','a')
           f = file.write(username.lower())
           file.write(' ')
           file.write (password.lower())
           file.write("\n")
           file.close()
        else:
           print("username exist")

    def login(self,Uname,Upass):
        flag = False
        for line in open('account.txt','r').readlines():
            if line.split(" ")[0] == Uname and line.split()[1] == Upass:
                flag = True
                break;
        return flag
                

if __name__ == "__main__":
    r = UserRegistration()
    def main_menu():
        print("|=====================================================|")
        print("|====Enter your choice :==============================|")
        print("|====If newer here, signup . So press 1:==============|")
        print("|====If already signup , please press 2 for login:====|")
        print("|=====================================================|")
        print("\n")
    main_menu()
    n = input()
    while n != "":
        if int(n) == 1:
            r.signup(input("enter username: "),input("enter password: "))
        elif int(n) == 2:
            inp=r.login(input("enter your username: "), input("enter your password: "))
            if inp:
                print("Successfully login")
            else:
                print("Invalid username or password,try again...")
        else:
            print("There have any operation")
        main_menu()
        n = input()
