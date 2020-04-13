class NoUserFound(Exception):

    def __init__(self, message='No found'):
        self.message = message

class NoDeviceFound(Exception):

    def __init__(self, message='No found'):
        self.message = message