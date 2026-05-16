import pytest
from models import Task
from processor import execute_task

def test_mutable_history_leak():
    # This test will FAIL initially due to Bug 3 (state leaks between calls)
    t1 = Task("task_A", "UPPERCASE", {"text": "a"})
    t2 = Task("task_B", "UPPERCASE", {"text": "b"})
    
    res1 = execute_task(t1)
    res2 = execute_task(t2) # If history is clean, res2's history snapshot should only have 1 item
    
    assert len(res2["history_snapshot"]) == 1
