import pytest
from models import Task
from queue_manager import TaskQueue

def test_priority_ordering():
    # This test will FAIL initially due to Bug 2 (returns lowest instead of highest)
    q = TaskQueue()
    t_low = Task("low", "UPPERCASE", {}, priority=1)
    t_high = Task("high", "UPPERCASE", {}, priority=10)
    
    q.add_task(t_low)
    q.add_task(t_high)
    
    assert q.next_task().task_id == "high"
