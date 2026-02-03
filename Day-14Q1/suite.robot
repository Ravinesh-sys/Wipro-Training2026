*** Settings ***
Library           SeleniumLibrary

Suite Setup       Open Browser And Maximize
Suite Teardown    Close All Browsers

Test Setup        Go To Home Page
Test Teardown     Capture Page Screenshot

*** Variables ***
${BROWSER}        Chrome
${URL}            https://www.google.com

*** Keywords ***
Open Browser And Maximize
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window

Go To Home Page
    Go To    ${URL}

*** Test Cases ***
Search In Google
    [Tags]    smoke    google
    Input Text    name=q    Robot Framework
    Press Keys    name=q    ENTER
    Sleep    2

Verify Page Title
    [Tags]    regression
    Title Should Be    Google
