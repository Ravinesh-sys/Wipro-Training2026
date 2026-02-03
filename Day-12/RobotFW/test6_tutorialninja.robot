*** Settings ***
Library    SeleniumLibrary
Test Template     Adding Values
Library       DataDriver    file=test6data.xlsx     sheet_name=Sheet1
Suite Setup    Open Website
Suite Teardown      Close Website

*** Variables ***
${URL}      https://tutorialsninja.com/demo/
${BROWSER}   edge

*** Keywords ***

Open Website
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Wait Until Element Is Visible  xpath=//i[@class="fa fa-user"]    10s

Adding Values
    [Arguments]        ${firstname}    ${lastname}   ${email}    ${telephone}        ${password}    ${confirm}
    Click Element    xpath=//*[@id="top-links"]/ul/li[2]/a
    sleep         1s
    Wait Until Element Is Visible    xpath=//*[@id="top-links"]/ul/li[2]/ul/li[1]/a
    sleep         1s
    Click Element    xpath=//*[@id="top-links"]/ul/li[2]/ul/li[1]/a
    sleep         1s
    Wait Until Element Is Visible    xpath=//*[@id="account"]/legend         10s
    Input Text    name=firstname     ${firstname}

    Input Text    name=lastname        ${lastname}

    Input Text     name=email                ${email}

    Input Text    name=telephone            ${telephone}

    Input Text    name=password            ${password}

    Input Text    name=confirm            ${confirm}

    Click Element    xpath=//*[@id="content"]/form/fieldset[3]/div/div/label[1]/input

    Click Element    xpath=//input[@name="agree"]

    Click Element    xpath=//input[@type="submit"]
    sleep             3s
    Wait Until Element Is Visible  xpath=//i[@class="fa fa-user"]    10s
    Capture Page Screenshot
    sleep             3s
    Click Element    xpath=//*[@id="top-links"]/ul/li[2]/a
    sleep             3s
    Click Element     xpath=//*[@id="top-links"]/ul/li[2]/ul/li[5]/a
    sleep             3s
    Wait Until Element Is Visible  xpath=//i[@class="fa fa-user"]    10s
    sleep             3s
    Click Element    xpath=//*[@id="top-links"]/ul/li[2]/a
    sleep             3s
    Click Element    xpath=//*[@id="top-links"]/ul/li[2]/ul/li[2]/a
    sleep             3s
    Wait Until Element Is Visible    xpath=//*[@id="content"]/div/div[2]/div/h2    5s

    Input Text        name=email           ${email}
    sleep             2s
    Input Text        name=password    ${password}
    sleep             3s
    Click Button    xpath=//input[@type='submit']
    sleep             3s
    Wait Until Element Is Visible   xpath=//*[@id="content"]/h2[1]  5s

    Capture Page Screenshot
    sleep             3s
    Wait Until Element Is Visible        xpath=//*[@id="account-account"]/ul/li[2]/a
    sleep             3s
    Click Element         xpath=//*[@id="top-links"]/ul/li[2]/a/i
    sleep             3s
    Click Element         xpath=//*[@id="top-links"]/ul/li[2]/ul/li[5]/a
    sleep             2s
Close Website
    Close Browser

*** Test Cases ***
Login with user

