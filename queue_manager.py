from models import Task

class TaskQueue:
    def __init__(self):
        self.queue = []

    def add_task(self, task: Task):
        """Adds a task to the queue."""
        self.queue.append(task)

    def next_task(self) -> Task:
        """Fetches and removes the highest priority task from the queue."""
        if not self.queue:
            return None
            
        # BUG 2: Sorts ascending (lowest priority first). 
        # Should be: self.queue.sort(key=lambda t: t.priority, reverse=True)
        self.queue.sort(key=lambda t: t.priority)
        
        return self.queue.pop(0)
