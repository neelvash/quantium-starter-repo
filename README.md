# Quantium Virtual Job Simulation: Pink Morsel Sales Visualiser

This repository contains my project for the **Quantium Software Engineering Virtual Job Simulation**, completed through **Forage**. 

In this simulation, I acted as a Software Engineer for Quantium, tasked with analysing historical sales data for a fictional client, **Soul Foods**, and building an interactive dashboard to visualise the sales of their flagship product, the "Pink Morsel". 

Beyond building the application, the simulation focused heavily on Software Engineering and DevOps best practices, including Test-Driven Development (TDD) and Continuous Integration (CI).

## Project Highlights
* **Interactive Data Visualisation:** A dynamic line chart built with Python, Dash, and Plotly Express that updates instantly based on user input.
* **Data Filtering:** Radio buttons allow users to slice sales data by region (North, East, South, West, or All) to identify regional trends.
* **Automated UI Testing:** A robust Pytest suite that utilises Dash's built-in testing framework (Selenium) to verify that critical DOM elements (headers, charts, and input controls) render correctly.
* **CI/CD Ready:** Authored a Bash script (`run_tests.sh`) that automatically activates virtual environments, executes the test suite, and returns standard exit codes (0 or 1) to pass or fail automated deployment pipelines.

## Tech Stack
* **Language:** Python, Bash
* **Data Processing:** Pandas
* **Frontend / Visualisation:** Plotly, Dash
* **Testing / QA:** Pytest, Selenium (Dash Testing)
* **Concepts Applied:** Data Visualisation, Automated Testing, Continuous Integration (CI)

## 📁 Repository Structure
```text
├── data/
│   └── formatted_sales_data.csv  # Cleaned and formatted sales data
├── app.py                        # Main Dash application and layout
├── test_app.py                   # Pytest suite for automated UI testing
├── run_tests.sh                  # Bash script for CI pipeline execution
├── requirements.txt              # Project dependencies 
└── README.md                     # Project documentation
```

## Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Set up the virtual environment
It is highly recommended to run this project in an isolated virtual environment.
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the application
```bash
python app.py
```
Once the server is running, open your web browser and navigate to `http://127.0.0.1:8050/` to view the dashboard!

## Running the Tests (CI/CD Simulation)

This project uses `pytest` alongside `dash.testing` to ensure the application renders exactly as expected without manual checks. To run the tests automatically using the provided Bash script (simulating a CI pipeline environment):

1. Ensure the script has executable permissions:
```bash
chmod +x run_tests.sh
```

2. Execute the test script:
```bash
./run_tests.sh
```

**Expected Output:**
The script will activate the virtual environment, run the test suite, and output an exit code. 
* **`Exit Code 0`**: All tests passed successfully.
* **`Exit Code 1`**: One or more tests failed (in a real world scenario, this would halt the CI/CD pipeline and block the code from being deployed).

---
*Certificate of completion for the Quantium Software Engineering Virtual Job Simulation is available upon request.*
