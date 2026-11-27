# Contributing to Desktop File Sorter

Thank you for your interest in improving Desktop File Sorter.

## Getting started

1. Fork or clone the repository.
2. Make sure Python 3.12 or newer is installed.
3. Install the project dependencies:

```bash
python -m pip install -r requirements.txt
```

4. Run the application:

```bash
python main.py
```

## Running tests

Run the test suite from the repository root:

```bash
python -m unittest discover -s tests -v
```

Please run the tests before submitting changes. If you add or change behavior, include tests that cover the expected result.

## Pull request guidelines

- Keep each pull request focused on one change.
- Explain the problem and the solution in the pull request description.
- Include clear steps to reproduce and verify behavior for bug fixes.
- Update the README when user-facing behavior or setup instructions change.
- Avoid committing personal files, temporary files, build outputs, or test data.

## Reporting bugs

When opening an issue, include:
- Your Windows and Python versions.
- The steps needed to reproduce the problem.
- What you expected to happen.
- What actually happened.
- Relevant error messages or screenshots (remove private information first).

Thanks for helping make Desktop File Sorter better.
