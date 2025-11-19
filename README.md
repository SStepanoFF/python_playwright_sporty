
# Mobile Web Automation Framework (Python + Playwright + Pytest)

This repository contains an automation framework for testing **Twitch mobile UI** using:

- **Python**
- **Playwright (Sync API)**
- **Pytest**
- **Allure Report**
- **HTML Pytest Report**

The tests run in **Chrome Mobile Emulation Mode**, support **headless/headed execution**, and follow the **Page Object Model (POM)**.

---

## 1. Clone the Repository

```bash
git clone https://github.com/SStepanoFF/python_playwright_sporty
```

---

## 2. Installation

### 2.1 Install Python (3.12+ recommended)

Download from: https://www.python.org/downloads/  

---

### 2.2 Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate         # macOS/Linux
# .venv\Scripts\activate        # Windows
```

---

### 2.3 Install project dependencies

```bash
pip install -r requirements.txt
```

---

### 2.4 Install Playwright Browsers

```bash
playwright install
playwright install-deps     # macOS & Linux only
```

---

### 2.5 Install Allure

#### macOS:

```bash
brew install allure
```

#### Windows:

Download from: https://github.com/allure-framework/allure2/releases

Validate installation:

```bash
allure --version
```

---

### 2.6 Install Pytest-HTML

```bash
pip install pytest-html
```

---

## 3. Test Execution

```bash
pytest
```

### Override configs

Run in headed mode:

```bash
pytest --headless=false
```

Use different mobile device:

```bash
pytest --mobile-device="iPhone 12"
```

Run a specific test:

```bash
pytest tests/test_mobile.py -v
```

---

## 4. Generate Allure Report

```bash
allure serve allure-results
```

Or generate static report:

```bash
allure generate allure-results -o allure-report --clean
allure open allure-report
```

---

## 5. Project Structure

```
project-root/
│
├── pages/
│   ├── base_page.py
│   ├── directory_page.py
│   ├── search_result_streamer_widget.py
│   ├── streamer_page.py
│   └── search_result_page.py
│
├── tests/
│   ├── conftest.py
│   └── test_search.py
│
├── pytest.ini
├── README.md
└── .venv/
```

---

# Framework Highlights

- Playwright Sync API  
- Mobile browser emulation (Chrome)  
- Page Object Model architecture  
- Pytest fixtures & config  
- Allure reporting  
- HTML reporting  
- Automatic screenshots  
- Supports headless/headed execution  
