import pytest
from notifier import dispatch_alert

def test_invalid_email_fallback():
    # This test will FAIL initially with NameError due to Bug 4
    result = dispatch_alert("bad_email_no_at_sign", "System Failure Alarm!")
    assert result is False
