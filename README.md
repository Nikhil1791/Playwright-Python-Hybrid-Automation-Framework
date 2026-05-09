# Playwright Python Hybrid Automation Framework

A scalable and maintainable Playwright Hybrid Automation Framework developed using Python, Pytest, Page Object Model (POM), Data Driven Testing, HTML Reporting, and CI/CD Integration.

---

# Tech Stack

- Python
- Playwright
- Pytest
- Page Object Model (POM)
- Pytest HTML Reports
- Data Driven Testing
- Utility Functions
- Logging
- Screenshot Capture
- GitHub Actions CI/CD

---

# Framework Features

- Page Object Model Design Pattern
- Reusable Utility Functions
- Cross Browser Testing
- HTML Reporting
- Screenshot on Failure
- Video Recording on Failure
- Trace Viewer Support
- Data Driven Framework
- Logging Mechanism
- Easy Maintenance
- Scalable Folder Structure
- CI/CD Integration

---

# Project Structure

```bash
playwright-python-framework
│
├── .github
│   └── workflows
│       └── playwright.yml
│
├── config
│   ├── config.py
│   └── test_data.json
│
├── pages
│   ├── login_page.py
│   ├── home_page.py
│   ├── cart_page.py
│   └── checkout_page.py
│
├── tests
│   ├── test_login.py
│   ├── test_add_to_cart.py
│   ├── test_checkout.py
│   ├── test_sort_products.py
│   └── test_logout.py
│
├── utils
│   ├── logger.py
│   ├── screenshot_util.py
│   ├── wait_util.py
│   ├── data_util.py
│   ├── common_util.py
│   └── retry_util.py
│
├── reports
├── screenshots
├── logs
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── run_tests.bat
└── README.md
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/Nikhil1791/Playwright-Python-Hybrid-Automation-Framework.git
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

---

## Activate Virtual Environment

### Windows

```bash
venv\\Scripts\\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Install Playwright Browsers

```bash
playwright install
```

---

# Run Test Cases

## Run All Tests

```bash
pytest
```

---

## Run Specific Test

```bash
pytest tests/test_login.py
```

---

## Run Tests in Parallel

```bash
pytest -n 2
```

---

## Generate HTML Report

```bash
pytest --html=reports/report.html --self-contained-html
```

---

# Framework Components

## Page Object Model (POM)

All locators and actions are separated into page classes for better reusability and maintainability.

---

## Utilities

Framework contains reusable utility files such as:

- Logger Utility
- Screenshot Utility
- Wait Utility
- Retry Utility
- Data Utility
- Common Utility

---

## Reporting

HTML reports are automatically generated after execution.

Report Path:

```bash
reports/report.html
```

---

## Screenshots & Videos

- Screenshots captured on failure
- Playwright trace and video support available

---

# Sample Test Scenarios

- Valid Login Test
- Invalid Login Test
- Add Product To Cart
- Complete Checkout Flow
- Product Sorting Validation
- Logout Functionality

---

# CI/CD Integration

GitHub Actions integration added for automated execution.

Workflow Path:

```bash
.github/workflows/playwright.yml
```

---

# Browser Support

- Chromium
- Firefox
- WebKit

---

# Author

Nikhil Dhamange

QA Automation Engineer

Skills:
- Selenium
- Playwright
- Python
- Pytest
- API Testing
- Jenkins
- Docker
- CI/CD
- Automation Framework Development

---

# Future Enhancements

- Docker Integration
- Allure Reporting
- Jenkins Pipeline
- Database Validation
- API + UI Hybrid Framework
- Cloud Execution Support
- Parallel Cross Browser Execution

---

# GitHub Repository Description

```bash
Playwright Python Hybrid Automation Framework using Pytest, POM, Data Driven Testing, HTML Reporting and CI/CD Integration.
```
