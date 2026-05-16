from models import Task
from queue_manager import TaskQueue
from processor import execute_task

def run_batch_pipeline():
    queue = TaskQueue()
    queue.add_task(Task("1", "UPPERCASE", {"text": "hello"}, priority=1))
    queue.add_task(Task("2", "REVERSE", {"text": "world"}, priority=2))
    queue.add_task(Task("3", "UPPERCASE", {"text": "test"}, priority=3))
    
    processed_count = 0
    
    # BUG 5: Modifying the queue length via next_task() while iterating over range(len(...)) 
    # dynamically shortens the list, meaning the loop ends prematurely and skips tasks.
    # Should be: while queue.queue: task = queue.next_task()
    for _ in range(len(queue.queue)):
        task = queue.next_task()
        if task:
            execute_task(task)
            processed_count += 1
            
    return processed_count

if __name__ == "__main__":
    print("Running pipeline...")
    count = run_batch_pipeline()
    print(f"Processed {count} tasks.")
