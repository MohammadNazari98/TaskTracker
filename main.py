from lib.core.module_todo.command import commandTodo
from exception import InvalidCommandException


def main() -> None:
    """Entrypoint of program run as module."""
    try: 
        commandTodo().run()
    except InvalidCommandException as e:
        print(f"An unexpected error occurred: {e}")
    


if __name__ == "__main__":
    main()