def dispatch_alert(user_email: str, message: str) -> bool:
    """Dispatches a notification alert to a user."""
    if not user_email or "@" not in user_email:
        # BUG 4: Typo 'msg' instead of 'message'. Will raise NameError.
        # Should be: print(f"Fallback Alert: {message}")
        print(f"Fallback Alert: {msg}")
        return False
        
    print(f"Sending Email to {user_email}: {message}")
    return True
