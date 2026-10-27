# tests/e2e/test_e2e.py

import pytest  # Import the pytest framework for writing and running tests

# The following decorators and functions define E2E tests for the FastAPI calculator application.

@pytest.mark.e2e
def test_hello_world(page, fastapi_server):
    # Navigate the browser to the homepage URL of the FastAPI application.
    page.goto('http://localhost:8000')
    
    # Use an assertion to check that the text within the first <h1> tag is exactly "Hello World".
    # If the text does not match, the test will fail.
    assert page.inner_text('h1') == 'Hello World'

@pytest.mark.e2e
def test_calculator_add(page, fastapi_server):
    # Navigate the browser to the homepage URL of the FastAPI application.
    page.goto('http://localhost:8000')
    
    # Fill in the first number input field (with id 'a') with the value '10'.
    page.fill('#a', '10')
    
    # Fill in the second number input field (with id 'b') with the value '5'.
    page.fill('#b', '5')
    
    # Click the button that has the exact text "Add". This triggers the addition operation.
    page.click('button:text("Add")')
    
    # Use an assertion to check that the text within the result div (with id 'result') is exactly "Result: 15".
    # This verifies that the addition operation was performed correctly and the result is displayed as expected.
    assert page.inner_text('#result') == 'Calculation Result: 15'



def test_calculator_subtract(page, fastapi_server):
    # Navigate the browser to the homepage URL of the FastAPI application.
    page.goto('http://localhost:8000')
    
    # Fill in the first number input field (with id 'a') with the value '10'.
    page.fill('#a', '10')
    
    # Fill in the second number input field (with id 'b') with the value '5'.
    page.fill('#b', '5')
    
    # Click the button that has the exact text "Subtract". This triggers the subtraction operation.
    page.click('button:text("Subtract")')
    
    # Use an assertion to check that the text within the result div (with id 'result') is exactly "Result: 5".
    # This verifies that the subtraction operation was performed correctly and the result is displayed as expected.
    assert page.inner_text('#result') == 'Calculation Result: 5'


def test_calculator_multiply(page, fastapi_server):
    # Navigate the browser to the homepage URL of the FastAPI application.
    page.goto('http://localhost:8000')
    
    # Fill in the first number input field (with id 'a') with the value '10'.
    page.fill('#a', '10')
    
    # Fill in the second number input field (with id 'b') with the value '5'.
    page.fill('#b', '5')
    
    # Click the button that has the exact text "multiply". This triggers the multiplication operation.
    page.click('button:text("multiply")')
    
    # Use an assertion to check that the text within the result div (with id 'result') is exactly "Result: 15".
    # This verifies that the multiply operation was performed correctly and the result is displayed as expected.
    assert page.inner_text('#result') == 'Calculation Result: 50'


def test_calculator_divide(page, fastapi_server):
    # Navigate the browser to the homepage URL of the FastAPI application.
    page.goto('http://localhost:8000')
    
    # Fill in the first number input field (with id 'a') with the value '10'.
    page.fill('#a', '10')
    
    # Fill in the second number input field (with id 'b') with the value '5'.
    page.fill('#b', '5')
    
    # Click the button that has the exact text "Divide". This triggers the division operation.
    page.click('button:text("Divide")')
    
    # Use an assertion to check that the text within the result div (with id 'result') is exactly "Result: 2.0".
    # This verifies that the division operation was performed correctly and the result is displayed as expected.
    assert page.inner_text('#result') == 'Calculation Result: 2'

def test_calculator_add_negative(page, fastapi_server):
    # Navigate the browser to the homepage URL of the FastAPI application.
    page.goto('http://localhost:8000')
    
    # Fill in the first number input field (with id 'a') with the value '10'.
    page.fill('#a', '10')
    
    # Fill in the second number input field (with id 'b') with the value '5'.
    page.fill('#b', '-5')
    
    # Click the button that has the exact text "Add". This triggers the addition operation.
    page.click('button:text("Add")')
    
    # Use an assertion to check that the text within the result div (with id 'result') is exactly "Result: 15".
    # This verifies that the addition operation was performed correctly and the result is displayed as expected.
    assert page.inner_text('#result') == 'Calculation Result: 5'

def test_calculator_subtract_negative(page, fastapi_server):
    # Navigate the browser to the homepage URL of the FastAPI application.
    page.goto('http://localhost:8000')
    
    # Fill in the first number input field (with id 'a') with the value '10'.
    page.fill('#a', '10')
    
    # Fill in the second number input field (with id 'b') with the value '5'.
    page.fill('#b', '-5')
    
    # Click the button that has the exact text "Subtract". This triggers the subtraction operation.
    page.click('button:text("Subtract")')
    
    # Use an assertion to check that the text within the result div (with id 'result') is exactly "Result: 15".
    # This verifies that the subtraction operation was performed correctly and the result is displayed as expected.
    assert page.inner_text('#result') == 'Calculation Result: 15'

def test_calculator_add_two_negatives(page, fastapi_server):
    # Navigate the browser to the homepage URL of the FastAPI application.
    page.goto('http://localhost:8000')
    
    # Fill in the first number input field (with id 'a') with the value '10'.
    page.fill('#a', '-10')
    
    # Fill in the second number input field (with id 'b') with the value '5'.
    page.fill('#b', '-5')
    
    # Click the button that has the exact text "Add". This triggers the addition operation.
    page.click('button:text("Add")')
    
    # Use an assertion to check that the text within the result div (with id 'result') is exactly "Result: 15".
    # This verifies that the addition operation was performed correctly and the result is displayed as expected.
    assert page.inner_text('#result') == 'Calculation Result: -15'

def test_calculator_subtract_two_negatives(page, fastapi_server):
    # Navigate the browser to the homepage URL of the FastAPI application.
    page.goto('http://localhost:8000')
    
    # Fill in the first number input field (with id 'a') with the value '10'.
    page.fill('#a', '-10')
    
    # Fill in the second number input field (with id 'b') with the value '5'.
    page.fill('#b', '-5')
    
    # Click the button that has the exact text "Subtract". This triggers the subtraction operation.
    page.click('button:text("Subtract")')
    
    # Use an assertion to check that the text within the result div (with id 'result') is exactly "Result: 15".
    # This verifies that the subtraction operation was performed correctly and the result is displayed as expected.
    assert page.inner_text('#result') == 'Calculation Result: -5'


def test_calculator_multiply_two_negatives(page, fastapi_server):
    # Navigate the browser to the homepage URL of the FastAPI application.
    page.goto('http://localhost:8000')
    
    # Fill in the first number input field (with id 'a') with the value '10'.
    page.fill('#a', '-10')
    
    # Fill in the second number input field (with id 'b') with the value '5'.
    page.fill('#b', '-5')
    
    # Click the button that has the exact text "multiply". This triggers the multiplication operation.
    page.click('button:text("multiply")')
    
    # Use an assertion to check that the text within the result div (with id 'result') is exactly "Result: 15".
    # This verifies that the multiply operation was performed correctly and the result is displayed as expected.
    assert page.inner_text('#result') == 'Calculation Result: 50'


def test_calculator_multiply_negative_and_positive(page, fastapi_server):
    # Navigate the browser to the homepage URL of the FastAPI application.
    page.goto('http://localhost:8000')
    
    # Fill in the first number input field (with id 'a') with the value '10'.
    page.fill('#a', '-10')
    
    # Fill in the second number input field (with id 'b') with the value '5'.
    page.fill('#b', '5')
    
    # Click the button that has the exact text "multiply". This triggers the multiplication operation.
    page.click('button:text("multiply")')
    
    # Use an assertion to check that the text within the result div (with id 'result') is exactly "Result: 15".
    # This verifies that the multiply operation was performed correctly and the result is displayed as expected.
    assert page.inner_text('#result') == 'Calculation Result: -50'



def test_calculator_divide_negative(page, fastapi_server):
    # Navigate the browser to the homepage URL of the FastAPI application.
    page.goto('http://localhost:8000')
    
    # Fill in the first number input field (with id 'a') with the value '10'.
    page.fill('#a', '-10')
    
    # Fill in the second number input field (with id 'b') with the value '5'.
    page.fill('#b', '5')
    
    # Click the button that has the exact text "Divide". This triggers the division operation.
    page.click('button:text("Divide")')
    
    # Use an assertion to check that the text within the result div (with id 'result') is exactly "Result: 2.0".
    # This verifies that the division operation was performed correctly and the result is displayed as expected.
    assert page.inner_text('#result') == 'Calculation Result: -2'



def test_calculator_divide_two_negatives(page, fastapi_server):
    # Navigate the browser to the homepage URL of the FastAPI application.
    page.goto('http://localhost:8000')
    
    # Fill in the first number input field (with id 'a') with the value '10'.
    page.fill('#a', '-10')
    
    # Fill in the second number input field (with id 'b') with the value '5'.
    page.fill('#b', '-5')
    
    # Click the button that has the exact text "Divide". This triggers the division operation.
    page.click('button:text("Divide")')
    
    # Use an assertion to check that the text within the result div (with id 'result') is exactly "Result: 2.0".
    # This verifies that the division operation was performed correctly and the result is displayed as expected.
    assert page.inner_text('#result') == 'Calculation Result: 2'


@pytest.mark.e2e
def test_calculator_divide_by_zero(page, fastapi_server):
    # Navigate the browser to the homepage URL of the FastAPI application.
    page.goto('http://localhost:8000')
    
    # Fill in the first number input field (with id 'a') with the value '10'.
    page.fill('#a', '10')
    
    # Fill in the second number input field (with id 'b') with the value '0', attempting to divide by zero.
    page.fill('#b', '0')
    
    # Click the button that has the exact text "Divide". This triggers the division operation.
    page.click('button:text("Divide")')
    
    # Use an assertion to check that the text within the result div (with id 'result') is exactly
    # "Error: Cannot divide by zero!". This verifies that the application handles division by zero
    # gracefully and displays the correct error message to the user.
    assert page.inner_text('#result') == 'Error: Cannot divide by zero!'
