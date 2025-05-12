# API Weather Tester

This project automates tests over a weather API using Python, PyTest and Visual Studio Code. It simulates a rea lscenario where a QA Tester automates public API validations that delivers meteorological data.

---

## Used technologies

- Python 3.x
- [Requests](https://pypi.org/project/requests/) – for API consumption
- [PyTest](https://docs.pytest.org/en/latest/) – to estructure and execute automated tests
- Visual Studio Code – main editor tool
- Git & GitHub – main version control

---

## 📂 Project structure

```plaintext
api_weather_tester/
│
├── src/                  # Main code
│   └── main.py
├── tests/                # Automated tests
│   └── test_weather_api.py
├── data/                 # test data
│   └── sample_cities.txt
├── reports/              # Logs o future results
│   └── README.txt
├── requirements.txt      # Project dependencies
├── .gitignore            # Git ignored files
└── README.md             # This file
```

---

## How to execute tests

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Execute tests with Pytest:
```bash
pytest tests/
```

---

## Implemented tests

- `test_weather_api_response_code`: Verifies that the API sends a 200
- `test_weather_api_structure`: Validates that the JSON response contains `location` and `current` keys

---

## Probable future implementations and improvements

- More field validation: temperature, humidity, wind, etc.
- Parameterized tests for multiple cities.
- Results comparison with expected values.
- `JSON Schema` integration for strict validations
- Results exports in HTML or JSON

---

## Notes

- This project uses the API: [weatherapi.com](https://www.weatherapi.com/), that requires a free API Key to work. You must replace `YOUR_API_KEY` in `src/main.py` with your real.

---

## Autor

This project was created as part of an advanced QA Automation practice using Python and Pytest.

---

## 🧾 HTML Test Report

After running the tests, an HTML report is automatically generated at:

```
reports/report.html
```

To view it, simply open that file in your browser.

If you're running the tests for the first time, make sure to install the plugin:

```bash
pip install pytest-html
```

The report provides a full visual overview of the test results, ideal for presentations or audits.
