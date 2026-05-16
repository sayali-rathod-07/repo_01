from models import Task

def execute_task(task: Task, history=[]) -> dict:
    """
    Simulates executing a task and logs it to history.
    BUG 3: Uses a mutable default argument for 'history'.
    Should be: 
    if history is None: history = []
    """
    if task.action == "UPPERCASE":
        result = task.payload.get("text", "").upper()
        task.status = "COMPLETED"
    elif task.action == "REVERSE":
        result = task.payload.get("text", "")[::-1]
        task.status = "COMPLETED"
    else:
        task.status = "FAILED"
        result = "Unknown Action"
        
    history.append(task.task_id)
    
    return {
        "task_id": task.task_id,
        "status": task.status,
        "result": result,
        "history_snapshot": list(history)
    }
