import time

class Task:
    def __init__(self, task_id: str, action: str, payload: dict, priority: int = 1):
        self.task_id = task_id
        self.action = action
        self.payload = payload
        self.priority = priority  # Higher number = higher priority
        self.status = "PENDING"
        self.retries = 0
        
        # BUG 1: The backoff factor is instantiated as a string instead of an integer.
        # Should be: self.backoff_factor = 2
        self.backoff_factor = "2" 

    def calculate_delay(self) -> int:
        """Calculates exponential backoff delay for retries."""
        # This will crash with a TypeError: unsupported operand type(s) for **: 'str' and 'int'
        return self.backoff_factor ** self.retries
