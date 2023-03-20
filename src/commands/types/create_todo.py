class CreateTodoCommand:
    def __init__(self, title: str, description: str, completed: bool = False):
        self.title = title
        self.description = description
        self.completed = completed
