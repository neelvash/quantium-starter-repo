#!/bin/bash

# 1. Activate the virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# 2. Execute the test suite
echo "Running the test suite..."
pytest test_app.py

# 3. Capture the exit code of the pytest command
TEST_EXIT_CODE=$?

# 4. Return exit code 0 if all tests passed, or 1 if something went wrong
if [ $TEST_EXIT_CODE -eq 0 ]; then
    echo "========================================="
    echo "SUCCESS: All tests passed successfully!"
    echo "========================================="
    exit 0
else
    echo "========================================="
    echo "FAILURE: One or more tests failed."
    echo "========================================="
    exit 1
fi