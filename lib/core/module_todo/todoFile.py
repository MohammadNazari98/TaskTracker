import os

class TodoFile:
    __FILENAME = "database.json"
        
    def createFileTodo(self) -> None:
        if not self.checkFileTodoExist():
            with open(self.__FILENAME,"w") as file:
                file.write("[]")
            
    def checkFileTodoExist(self) -> bool:
        return os.path.exists(self.__FILENAME)
    
    def readFileTodo(self) -> str:
        with open(self.__FILENAME,"r") as file:
            data = file.read()
        return data
    
    def writeFileTodo(self,content:str):
        with open(self.__FILENAME,"w") as file:
            file.write(content)