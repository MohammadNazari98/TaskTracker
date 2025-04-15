import argparse
from exception import InvalidCommandException
from lib.core.module_todo.todo import TodoList


class commandTodo:
    todos = TodoList() 
    def run(self) -> None:
        parser = argparse.ArgumentParser(description="Task tracker")
        subparsers = parser.add_subparsers(dest="command",help="Available command")
        # command: list
        list_command = subparsers.add_parser("list",help="list tasks by status.")
        list_command.add_argument("status",nargs="?",default="",help="Status filter:Todo,done,in-progress")
        # command: add
        add_parser = subparsers.add_parser("add",help="add a new task.")
        add_parser.add_argument("description",help="Task description")
        # command: update
        update_parser = subparsers.add_parser("update",help="update a task's description")
        update_parser.add_argument("id",type=int,help="Task ID")
        update_parser.add_argument("description",help="New description")
        # command: delete
        delete_parser = subparsers.add_parser("delete",help="Delete a task")
        delete_parser.add_argument("id",type=int,help="Task ID")
        # command: mark-in-progress
        mark_in_progress = subparsers.add_parser("mark-in-progress",help="Mark task as in-progress")
        mark_in_progress.add_argument("id",type=int,help="Task ID")
        # command: mark-done
        mark_done = subparsers.add_parser("mark-done",help="Mark task as done")
        mark_done.add_argument("id",type=int,help="Task ID")
        
        args = parser.parse_args()
        command = args.command
        
        if command == "list":
            self.todos.showMarkListTodo(args.status)
        elif command == "add":
            self.todos.addTodo(args.description)
        elif command == "delete" :
            self.todos.deleteTodo(args.id)
        elif command == "update":
            self.todos.updateTodo(args.id,args.description)
        elif command == "mark-in-progress":
            self.todos.markingTodo(args.id,"in-progress")
        elif command == "mark-done":
            self.todos.markingTodo(args.id,"done")
        else:
            raise InvalidCommandException(args.command)