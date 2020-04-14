
import bcrypt

# Default is 12 rounds

def generatePassEncripted(password):
    password = password.encode()
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password, salt).decode("utf-8") 


def checkPassword(text, password):
    if bcrypt.checkpw(text.encode(), password.encode()):
        return True
    else:
        return False
