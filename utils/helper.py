class HelperFunctions:

    @staticmethod
    def safe_action_decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except ValueError as e:
                print(f"Error: {e}")
                return None
        return wrapper