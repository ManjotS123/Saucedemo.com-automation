# SauceDemo Automation Test Framework

End-to-end automation framework for the [SauceDemo](https://www.saucedemo.com)
web application, built with **Playwright (Python)** and **Pytest**. Tests run
against both **desktop** and **emulated mobile** browsers, are containerised with
**Docker**, and run in **GitHub Actions** with JUnit reporting and failure
screenshots.

## Overview

The suite validates the core SauceDemo user journey i.e login, product browsing,
cart, and checkout using the Page Object Model. Mobile coverage is provided by
Playwright's built-in **device emulation**, so every test runs on a desktop context and a mobile viewport from a
single codebase.

- Built with **Playwright (Python)** and **Pytest**
- **25 UI tests**, executed across **desktop and mobile chrome (Pixel 5)** 
- Page Object Model for maintainable, reusable page logic
- Environment-driven configuration (URL, credentials, headless, device matrix)
- **JUnit XML** reports + automatic screenshots on every test
- Runs in **Docker** and **GitHub Actions CI**

## Prerequisites

- Python 3.11+
- Git

## Setup

```bash
# Install dependencies
pip install -r requirements.txt

# Install Playwright browsers 
playwright install chromium
```

## Running the tests

```bash
# Run the full suite from the repo root
pytest

# Run a single test file
pytest UI/POM/Tests/test_checkout.py

# Run only the desktop or mobile variant
pytest -k "desktop"
pytest -k "Pixel 5"
```

## Configuration

All settings are environment variables with sensible defaults (see
`UI/POM/utils/config.py`):

| Variable               | Default                     | Description                                              |
| ---------------------- | --------------------------- | -------------------------------------------------------- |
| `SAUCEDEMO_BASE_URL`   | `https://www.saucedemo.com` | Target application URL                                   |
| `SAUCEDEMO_USERNAME`   | `standard_user`             | Login username                                           |
| `SAUCEDEMO_PASSWORD`   | `secret_sauce`              | Login password                                           |
| `HEADLESS`             | `true`                      | Set `false` to watch the browser locally                |
| `PLAYWRIGHT_DEVICES`   | `desktop,Pixel 5`           | Comma-separated device matrix (`desktop` + any Playwright device descriptor, e.g. `iPhone 13`) |

Examples:

```bash
# Watch a desktop-only run in a headed browser
HEADLESS=false PLAYWRIGHT_DEVICES=desktop pytest

# Test a different device matrix
PLAYWRIGHT_DEVICES="desktop,iPhone 13,iPad Mini" pytest

# Test as the locked-out user
SAUCEDEMO_USERNAME=locked_out_user pytest UI/POM/Tests/test_login.py
```

## Docker

```bash
# Build the image
docker build -t saucedemo-tests .

# Run the suite (mount volumes to retrieve the report and screenshots)
docker run --rm \
  -v "$(pwd)/reports:/app/reports" \
  -v "$(pwd)/Screenshots:/app/Screenshots" \
  saucedemo-tests
```

The base image (`mcr.microsoft.com/playwright/python`) ships with the matching
browsers preinstalled, and tests run headless by default.

## Continuous Integration

`.github/workflows/test.yaml` runs the suite on **push** and **pull requests** to
`main`, and on manual dispatch:

- Runs on `ubuntu-latest` with Python 3.11
- Installs dependencies from `requirements.txt` and Playwright browsers
- Executes `pytest UI/POM/Tests`
- Uploads `reports/results.xml` and `Screenshots/` as build artifacts (even on failure)

## License

See [`licenses/LICENSE.txt`](licenses/LICENSE.txt) (Zope Public License 2.1).
