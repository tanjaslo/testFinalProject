# testFinalProject

testFinalProject is a Python automation project that tests a https://six-cities-7.vercel.app/ website using Selenium for UI testing and API requests. It's built with the PyCharm and PyTest tools and uses Page Object Modules for organized and maintainable code. The project manages dependencies with Poetry and generates test reports using pytest-html for clear documentation.

## Table of Contents

- [Project Overview](#project-overview)
- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [License](#license)

## Project Overview

MyProject is designed to automate testing of a web application using Selenium for UI testing and API requests for API testing. It covers various test scenarios and cases to ensure the application's functionality and data consistency.

## Installation

1. Clone this repository to your local machine.

    ```shell
    git clone https://github.com/tanjaslo/testFinalProject.git
    ```

2. Navigate to the project directory.

    ```shell
    cd testFinalProject
    ```

3. Use Poetry to install project dependencies and create a virtual environment.

    ```shell
    poetry install
   ```
   
4. Activate the virtual environment.

    ```shell
    poetry shell
    ```
5. Make sure you have Chrome WebDriver installed and added to your system's PATH. You can download Chrome WebDriver for your system from [here](https://chromedriver.chromium.org/downloads).

   
## Usage

To use testFinalProject, follow these steps:

1. Run the API tests:

    ```shell
    pytest tests/test_api.py
    ```
   
2. Run the Selenium UI and functionality tests:
    
    ```shell
    pytest tests/test_functionality.py
    ```
   
3. Run the Sign In and Sign Out tests:

    ```shell
    pytest tests/test_sign_in.py
    ```

Make sure to run the tests from the project directory.

## Generating Test Report

After running your tests, you can generate a detailed test report using `pytest-html`. Follow these steps to create the report:

1. Run your tests with the `--html` option to specify the output HTML report file. For example, to generate a report named `test_report.html`, use the following command:

   ```shell
   pytest --html=test_report.html
   ```

## Testing

### Test Scenarios

- API Testing for verifying data consistency and accuracy.
- Functionality Testing for interaction with web elements with the primary focus on verifying the functionality of the application.
- User Sign In and Sign Out testing for verifying user authentication.

### Test Cases

#### API Testing (test_api.py):

1. Verify successful API connection.
2. Verify data consistency and accuracy.
3. Verify that each place has a title.
4. Verify that place ratings are within the valid range (0.0 - 5.0).
5. Verify that place prices are positive.

#### Functionality Testing (test_functionality.py):

1. Verify that the page displays the expected number of cities.
2. Click on the city link and verify that the city link is active.
3. Click on the city link and verify that the city-specific page is loaded correctly.

#### User Sign In and Sign Out (test_sign_in.py):

1. User Signin with valid credentials.
2. User Sign Out.
3. User Signin with invalid credentials.

## License

This project is licensed under the [MIT License](LICENSE).
