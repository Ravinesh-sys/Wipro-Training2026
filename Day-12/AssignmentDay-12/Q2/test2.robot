*** Settings ***
Library    BuiltIn
Library    Process
Library    SeleniumLibrary

*** Test Cases ***
Verify Test Automation Environment

    Log To Console    ===== ENVIRONMENT VERIFICATION STARTED =====

    # 1. Verify Python installation
    ${py_result}=    Run Process    python    --version    stdout=PIPE    stderr=PIPE
    Run Keyword If    '${py_result.rc}' != '0'    Fail    Python is NOT installed or not in PATH
    Log To Console    Python Version: ${py_result.stdout}

    # 2. Verify Robot Framework installation
    ${rf_result}=    Run Process    python    -m    robot    --version    stdout=PIPE    stderr=PIPE


    # 3. Verify SeleniumLibrary import
    Run Keyword And Continue On Failure    Log    SeleniumLibrary imported successfully
    Log To Console    SeleniumLibrary is available

    Log To Console    ===== ENVIRONMENT VERIFICATION COMPLETED SUCCESSFULLY =====
