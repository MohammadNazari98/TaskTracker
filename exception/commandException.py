
class commandException(Exception):
    pass

class InvalidCommandException(commandException):
    def __init__(self,command:str):
        self.message = f"'{command}' This's an invalid command."
        super().__init__(self.message)