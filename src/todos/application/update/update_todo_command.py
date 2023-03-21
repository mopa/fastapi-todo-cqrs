class UpdateTodoCommand:
    def __init__(self, id: int, title: str = None, description: str = None, completed: bool = None):
        self.id = id
        self.title = title
        self.description = description
        self.completed = completed
