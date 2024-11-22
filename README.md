# OMDb API Testing 
This project involves testing the [OMDb API](https://www.omdbapi.com/), which is a RESTful web service that provides movie information. The goal is to practice and develop skills in API automation testing, implementing positive and negative tests to ensure robust API behavior and error handling. I also utilized Postman for exploratory testing. An HTML report is generated, which includes a summary of the test results.

## Technologies
- Python
- Requests
- pytest

## Prerequisites
- Have Python 3.x installed on your system

## Getting Started
1. Get a free API key at https://www.omdbapi.com/apikey.aspx
2. Create a virtual environment
    ```
    python3 -m venv venv
    ```
3. Activate the virtual environment
    - On Windows
        ```
        venv\Scripts\activate
        ```
    - On Mac/Linux
        ```
        source venv/bin/activate
        ```
4. Clone the repository
    ```
    git clone https://github.com/Brian1226/OMDb-API-testing.git
    ```
5. Install the required dependencies
    ```
    pip3 install -r requirements.txt
    ```
6. Create a `.env` file in the root directory and enter the base API URL and your API key
    ```
    BASE_URL = https://www.omdbapi.com/
    API_KEY = your_api_key_here
    ```
7. Run the tests and generate a report
    ```
    python3 -m pytest --html=reports/report.html --self-contained-html
    ```
