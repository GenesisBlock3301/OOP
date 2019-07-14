
userNameList = list()
class UserRegistration:

    def __init__(self):
        pass

    def signup(self,username, password):
        #read file line by line 
        for i in open('account.txt','r').readlines():
            #append existance username
            if username == i.split()[0]:
                userNameList.append(i.split()[0])
        if username not in userNameList:
            file = open('account.txt','a')
            f = file.write(username.lower())
            file.write(' ')
            file.write (password.lower())
            file.write("\n")
            file.close()
            return True
        else:
            print("username exist")
        return False

    def login(self,Uname,Upass):
        for line in open('account.txt','r').readlines():
            if line.split()[0] == Uname and line.split()[1] == Upass:
                print("Correct credential")
                return True
        print("Incorrect credential")
        return False

if __name__ == "__main__":
    r = UserRegistration()
    print("Enter your choice :")
    print("If newer here, signup . So press 1")
    print("If already signup , please press 2 for login: ")
    n = int(input())
    if n == 1:
        username = input("enter username: ")
        password = input("enter password: ")
        r.signup(username, password)
    elif n == 2:
        r.login(input("enter your username: "), input("enter your password: "))
    else:
        print("There haven't such operation")
