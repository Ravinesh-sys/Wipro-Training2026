*** Settings ***
Library    SeleniumLibrary
Library    DataDriver    file=testdata.xlsx    sheet_name=Sheet1
Test Template    OrangeHRM Login With Excel
Suite Setup    Open OrangeHRM
Suite Teardown    Close OrangeHRM

*** Variables ***
${URL}      https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
${BROWSER}  firefox

*** Test Cases ***
TC006_DDExcel_Login

*** Keywords ***
Open OrangeHRM
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Sleep    3s

Close OrangeHRM
    Close Browser

OrangeHRM Login With Excel
    [Arguments]    ${username}    ${password}
    Input Text    name=username    ${username}
    Input Text    name=password    ${password}
    Sleep    2s
