*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}      https://example.com
${BROWSER}  chrome
${TITLE}    Example Domain

*** Test Cases ***
Verify Page Title and Capture Screenshot
    Open Browser    ${URL}    ${BROWSER}
    Title Should Be    ${TITLE}
    Capture Page Screenshot
    Close Browser
