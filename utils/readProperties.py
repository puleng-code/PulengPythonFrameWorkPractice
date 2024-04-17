import configparser

config = configparser.RawConfigParser()  # getting Configurations>inputDate> data
config.read("./Configurations/inputData.ini")


class ReadConfig():
    @staticmethod
    def getBaseURL():
        BaseURL = config.get('Login Details', 'BaseURL')

    @staticmethod
    def getUserName():
        Username = config.get('Login Details', 'Username')

    @staticmethod
    def getPassword():
        Password = config.get('Login Details', 'Password')

    @staticmethod
    def getFirstName():
        FirstName = config.get('User Information', 'FirstName')

    @staticmethod
    def getLastName():
        LastName = config.get('User Information', 'LastName')

    @staticmethod
    def getZipCode():
        ZipCode = config.get('User Information', 'ZipCode')
