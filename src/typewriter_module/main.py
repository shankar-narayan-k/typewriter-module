import functools
import time


def typewriter_decorator(delay=0.05):
    """
    A decorator that intercepts print calls from a function
    and outputs the characters with a typewriter effect.
    """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Access the original built-in print function
            import builtins

            original_print = builtins.print

            # Define an altered print function that prints character-by-character
            def typewriter_print(*print_args, sep=" ", end="\n", flush=False):
                # Join multiple arguments like normal print does (e.g. print("A", "B"))
                full_text = sep.join(str(arg) for arg in print_args) + end

                for char in full_text:
                    original_print(char, end="", flush=True)
                    time.sleep(delay)

            # Temporarily overwrite the built-in print within this execution scope
            builtins.print = typewriter_print
            try:
                result = func(*args, **kwargs)
                # Add the slight video pause after execution finishes
                time.sleep(1)
                return result
            finally:
                # Restore original print to avoid side-effects elsewhere
                builtins.print = original_print

        return wrapper

    return decorator


def main():
    # --- Usage Example ---

    @typewriter_decorator(delay=0.04)
    def greet_user(name):
        print(f"Hello, {name}!")
        print("Welcome to the typewriter module.")

    greet_user("Developer")

    # https://g.co/gemini/share/a60a61c8407e

if __name__ == "__main__":
	main()
