import json
from typing import TypedDict ,List
from datetime import datetime
from tabulate import tabulate
from lib.core.module_todo.todoFile import TodoFile


class TodoType(TypedDict):
    description: str
    status: str
    createdAt: str
    updatedAt: str

class Todo:
    def __init__(self,description:str,status:str,createdAt:str,updatedAt:str):
        self._description:str = description
        self._status:str = status
        self._createdAt:str = createdAt
        self._updatedAt:str = updatedAt
    
    def createTodo(self) -> TodoType:
        return {
            "description":self._description,
            "status":self._status,
            "createdAt":self._createdAt,
            "updatedAt":self._updatedAt
            }
    
class TodoList:
    def __init__(self):
        self.todoFile = TodoFile()
        self._fileData = self.todoFile.readFileTodo()
        try:
            self.todos: List[TodoType] = json.loads(self._fileData)
        except json.JSONDecodeError:
            self.todos = []
    
    def addTodo(self,description:str) -> None:
        newTodo = Todo(description,"todo",datetime.now().strftime("%d/%m/%Y, %H:%M:%S"),datetime.now().strftime("%d/%m/%Y, %H:%M:%S"))
        todoDict = newTodo.createTodo()
        if self.todos:
            last_id = max(todo["id"] for todo in self.todos)
        else:
            last_id = 0
        todoDict["id"] = last_id + 1
        self.todos.append(todoDict)
        self.todoFile.writeFileTodo(json.dumps(self.todos,indent=2))
        
    def findTodo(self,id:int) -> TodoType | None:
        found = next((todo for todo in self.todos if todo["id"] == id),None)
        return found
        
    def updateTodo(self,id:int,new_description) -> None:
        todo = self.findTodo(id)
        if todo is None:
            print(f"Todo with id {id} not found.")
            return
        todo["description"] = new_description
        todo["updatedAt"] = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        self.todoFile.writeFileTodo(str(json.dumps(self.todos)))
        print(f"Todo with id {id} has been updated.")
        
    def deleteTodo(self,id : int) -> None:
        todo = self.findTodo(id)
        if todo is None:
            print(f"Todo with id {id} not found.")
            return
        self.todos.remove(todo)
        self.todoFile.writeFileTodo(str(json.dumps(self.todos)))
        print(f"Todo with id {id} has been deleted.")
    
    def markingTodo(self,id:int,mark:str):
        # add mark in progress to todo.
        # add mark done to todo. 
        todo = self.findTodo(id)
        if todo is None:
            print(f"Todo with id {id} not found.")
            return
        todo["status"] = mark
        todo["updatedAt"] = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        self.todoFile.writeFileTodo(str(json.dumps(self.todos)))
        print(f"Todo with id {id} has been updated.")
        
    def showMarkListTodo(self,mark:str):
        # show mark in progress todo.
        # show mark done todo.
        # show mark todo.
        self.todoFile.createFileTodo()
        file_content = self.todoFile.readFileTodo()
        try:
            self.todos = json.loads(file_content)
        except json.JSONDecodeError:
            print("Reading file json error.")
            return
        filtered_todos = (
            self.todos if mark == "" else [todo for todo in self.todos if todo["status"] == mark]
        )
        if not filtered_todos:
            print("There aren't any todo in the list.")
            return
        else:
            headers = ["ID","description","status","created at","updated at"]
            table = [
        [todo.get("id", ""), todo["description"], todo["status"], todo["createdAt"], todo["updatedAt"]]
        for todo in filtered_todos
    ]
            print(tabulate(table, headers=headers, tablefmt="fancy_grid"))