# PyBootstrap: Skeleton of automated test

## Tech Stack

- Test Runner: PyTest
- Build Tools: Poetry
- Web automation: Playwright Python
- API automation: Requests

## Setup

### Install Poetry

```bash
pip install poetry
```

### Install Dependencies

```bash
poetry install --no-root
```

### Install playwright

```bash
playwright install
```

## Run Tests

```bash
poetry run pytest

# Shows the browser while testing
./run.sh test_web
```