# Outstanding Concerns

These are review concerns not already addressed by the requested changes.

## Global monkey-patching

The decorator temporarily replaces `builtins.print`.

Potential implications:

- Not thread-safe.
- May affect concurrent code that prints while the decorated function is running.
- Nested decorated functions may have surprising interactions.

## Testing

The repository currently has no automated tests.

Recommended:

- pytest
- capsys-based output tests
- parameterized tests for delay, cursor, and stream behavior

## Public API

Consider re-exporting the decorator from the package root so users can write:

```python
from typewriter_module import typewriter_decorator
```

instead of importing from `main`.

## Release Process

Future releases would benefit from:

- GitHub Actions CI
- Automated test execution
- PyPI publishing workflow
- Versioning strategy (SemVer)