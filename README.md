# typewriter

A lightweight decorator-based typewriter effect for terminal output.

## Installation

```bash
uv add typewriter
```

## Usage

```python
from typewriter import typewriter

@typewriter(
    delay=0.04,
    cursor=True,
    random_delay=True,
    final_pause=0,
)
def greet():
    print("Hello World!")
    print("Welcome to the typewriter.")

greet()
```

## Parameters

| Parameter | Description |
|------------|-------------|
| `delay` | Base delay between characters |
| `cursor` | Displays a cursor while typing |
| `random_delay` | Adds natural variation to typing speed |
| `final_pause` | Pause after function execution completes |
| `stream` | Output stream (defaults to `sys.stdout`) |

## Design

This package is intentionally designed around a **decorator API**. The goal is to apply a typewriter effect to all `print()` calls within a function without changing the function body itself.

## Inspiration

Inspired by the [Indently](https://youtube.com/@indently)'s YouTube short [“I love the typewriter effect in Python”](https://youtube.com/shorts/88wzaOkV2mU).

## My Light bulb Moment

[can we make it a decorator so that all print statements from the function prints with this effect?...](https://youtube.com/shorts/88wzaOkV2mU?lc=UgzECUVaXXt6d3QnjHB4AaABAg)

## Disclaimer

AI has been used in every step of this project, but the decisions are made by a human.

The original proof-of-concept from Gemini's answer ([Python Typewriter Effect Code](https://g.co/gemini/share/4bee9496ea9c)) was refined and created as this reusable Python package.