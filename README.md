# mechanotrack

[![License](https://img.shields.io/pypi/l/mechanotrack.svg?color=green)](https://github.com/kevinyamauchi/mechanotrack/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/mechanotrack.svg?color=green)](https://pypi.org/project/mechanotrack)
[![Python Version](https://img.shields.io/pypi/pyversions/mechanotrack.svg?color=green)](https://python.org)
[![CI](https://github.com/kevinyamauchi/mechanotrack/actions/workflows/ci.yml/badge.svg)](https://github.com/kevinyamauchi/mechanotrack/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/kevinyamauchi/mechanotrack/branch/main/graph/badge.svg)](https://codecov.io/gh/kevinyamauchi/mechanotrack)

🚨 This repo is still under construction. Please check back later. 🚨

Tracking mechanical properties over time.

## Development

The easiest way to get started is to use the [github cli](https://cli.github.com)
and [uv](https://docs.astral.sh/uv/getting-started/installation/):

```sh
gh repo fork kevinyamauchi/mechanotrack --clone
# or just
# gh repo clone kevinyamauchi/mechanotrack
cd mechanotrack
uv sync
```

Run tests:

```sh
uv run pytest
```

Lint files:

```sh
uv run pre-commit run --all-files
```
