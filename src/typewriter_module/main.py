import functools
import random
import sys
import time


def typewriter_decorator(
    delay=0.05,
    cursor=True,
    random_delay=True,
    final_pause=0,
    stream=sys.stdout,
):
    """
    Decorator that intercepts print calls from a function and renders them
    with a typewriter effect.

    Parameters
    ----------
    delay : float
        Base delay between characters.
    cursor : bool
        Show a trailing cursor while typing.
    random_delay : bool
        Add small random variation to typing speed.
    final_pause : float
        Pause after the wrapped function completes.
    stream : file-like object
        Output stream to write to.

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
                full_text = sep.join(str(arg) for arg in print_args)

                for char in full_text:
                    stream.write(char)

                    current_delay = delay
                    if random_delay:
                        current_delay *= random.uniform(0.7, 1.3)

                    if cursor:
                        stream.write("|")
                        stream.flush()
                        time.sleep(max(0, current_delay * random.random() * 5))
                        stream.write("\b \b")

                    stream.flush()

                    time.sleep(max(0, current_delay))

                stream.write(end)
                stream.flush()

            builtins.print = typewriter_print

            try:
                result = func(*args, **kwargs)

                # Add the slight video pause after execution finishes
                if final_pause > 0:
                    time.sleep(final_pause)

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
