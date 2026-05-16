import pytest
from main import run_batch_pipeline

def test_batch_pipeline_completes_all_tasks():
    # This test will FAIL initially due to Bug 5 (skips tasks during loop iteration)
    processed = run_batch_pipeline()
    assert processed == 3
