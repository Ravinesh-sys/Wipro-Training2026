import time

def log_execution(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"[LOG] Method {func.__name__}() executed successfully")
        return result
    return wrapper


def performance_timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"[TIMER] Execution Time: {end - start:.4f} seconds")
        return result
    return wrapper


def admin_only(func):
    def wrapper(*args, **kwargs):
        is_admin = kwargs.get("is_admin", False)
        if not is_admin:
            print("Access Denied: Admin privileges required")
            return None
        return func(*args, **kwargs)
    return wrapper
