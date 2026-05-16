import pytest
from models import Task

def test_exponential_backoff_delay():
    # This test will FAIL initially with TypeError due to Bug 1
    task = Task("t1", "UPPERCASE", {"text": "abc"})
    task.retries = 2
    assert task.calculate_delay() == 4
