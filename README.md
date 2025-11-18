# Saucedemo.com Automation Test Framework

Automation framework for **SauceDemo** built using **Playwright** and **Pytest**, fully integrated with CI pipelines and automated reporting.

---

## Overview

This repository contains an end-to-end automation suite that validates the core functionality of the SauceDemo web application — from login to checkout.

-  Built with **Playwright (Python)**
-  Executed using **Pytest**
-  Integrated into **GitHub Actions CI**
-  Generates **JUnit test reports** for every run

---

## Features

###  End-to-End Test Coverage
Includes **24 automated E2E tests** covering the complete user journey:
- Login  
- Product browsing  
- Adding items to cart  
- Checkout workflow  
- Order completion  

### Playwright-Powered Automation
- Fast browser execution  
- Auto-waiting mechanisms  

### Pytest Test Runner
- Fixtures for setup/teardown  
- Clean test structure  
- Easy scalability  

### CI/CD Integration with GitHub Actions
- Automatically executes tests on every push, PR, or manual workflow  
- Maintains quality gates  
- Uploads test results as CI artifacts  

### JUnit Test Reporting
- Machine-readable XML reports  
- CI-compatible output  

---

