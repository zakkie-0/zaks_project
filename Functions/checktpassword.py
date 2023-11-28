def check_password(password):

    def isEightCharactersLong(password):
        if len(password) >= 8:
            return True
        else:
            return False

    def isAtleastHaveOneUpper(password):
        return any(eachChar.isupper() for eachChar in password)

    def isAtleastHaveOneLower(password):
        return any(eachChar.islower() for eachChar in password)

    def isAtleastHaveOneNumber(password):
        return any(eachChar.isdigit() for eachChar in password)

    if isAtleastHaveOneLower(password) == True and isAtleastHaveOneNumber(password) == True and isAtleastHaveOneUpper(password) == True and isEightCharactersLong(password) == True:
        return """That's a good password"""
    else:
        return """That isn't a good password"""


def display(password):

    return check_password(password)


print(display("CHDS4all"))
