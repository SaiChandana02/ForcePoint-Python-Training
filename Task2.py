from operator import truediv

class ContactDetails:
    def __init__(self,contactDetailsId,contactType,email):
        self.ContactDetailsId = contactDetailsId
        self.contactType = contactType
        self.email = email

class Contact:
    isActive = True
    def __init__(self,contactID,firstName,lastName):
        self.contactID = contactID
        self.firstName = firstName
        self.lastName = lastName


class User:
    isActive = True
    isAdmin = False
    contacts = []
    def __init__(self,userID,firstName,lastName,isAdmin):
        self.userID = userID
        self.firstName = firstName
        self.lastName = lastName
        self.isAdmin = isAdmin

    def createUser(self,userID,fName,LName):
        if self.isAdmin ==False:
            print("you are not admin you cannot create a new user")
            return
        newUser = User(userID,fName,LName,False)
        return newUser    

    def readUserData(self,user):
        if self.isAdmin == False:
           print("you are not admin you cannot read a user's data")
           return    
        if user.isActive == False:
            print("user is not active")
            return
        print("user First Name "+user.firstName)
        print("user Last Name "+user.lastName)
        print("user userId "+user.userID)
        if user.isAdmin == False:
            print("user is staff")
        else:
            print("user is Admin")
       
    def updateUserInfo(self,user,fName,LName,userId,isAdmin,isActive):
        if self.isAdmin == False:
           print("you are not admin you cannot update a user's data")
           return  
        if user.isActive == False:
           print("user is not active")
           return  
        user.firstName = fName
        user.lastName = LName
        user.userId = userId
        user.isAdmin = isAdmin
        user.isActive = isActive

    def deleteAUser(self,user):
        if self.isAdmin == False:
           print("you are not admin you cannot delete a user's data")
           return  
        user.isActive = False
        return
