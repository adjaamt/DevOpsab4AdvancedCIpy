# DevOps Lab 4 - Advanced CI with Python

This project demonstrates advanced Continuous Integration (CI) practices using Python, GitHub Actions, and various testing and linting tools.

## Project Structure

```
DevOpsab4AdvancedCIpy/
├── src/
│   └── calculator.py          # Main calculator module
├── tests/
│   └── test_calculator.py     # Test cases
├── .github/
│   └── workflows/
│       └── ci.yml            # GitHub Actions CI workflow
├── requirements.txt          # Python dependencies
├── setup.py                 # Package setup
├── pyproject.toml           # Tool configurations
├── .flake8                  # Flake8 linting config
└── README.md               # This file
```

## Features

- **Multi-stage CI pipeline** with linting, testing, and building
- **Matrix builds** across Python versions and operating systems
- **Dependency caching** for faster CI runs
- **Code coverage** reporting
- **Multiple linting tools**: flake8, black, mypy
- **Testing framework**: pytest with coverage

## Local Development

1. **Set up virtual environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run linting:**
   ```bash
   flake8 src tests
   black --check src tests
   mypy src
   ```

4. **Run tests:**
   ```bash
   pytest
   ```

5. **Run with coverage:**
   ```bash
   pytest --cov=src --cov-report=html
   ```

## CI Pipeline

The GitHub Actions workflow includes:

1. **Matrix Strategy**: Tests on Python 3.8, 3.9, 3.10, 3.11 across Ubuntu and Windows
2. **Caching**: Virtual environment dependencies are cached
3. **Lint Stage**: Runs flake8, black, and mypy
4. **Test Stage**: Runs pytest with coverage
5. **Build Stage**: Creates distribution packages
6. **Artifacts**: Uploads test reports and coverage data

## Tools Used

- **pytest**: Testing framework
- **pytest-cov**: Coverage reporting
- **flake8**: Linting and style checking
- **black**: Code formatting
- **mypy**: Static type checking
- **GitHub Actions**: CI/CD platform
