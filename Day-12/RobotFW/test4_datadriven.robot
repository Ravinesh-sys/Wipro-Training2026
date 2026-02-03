*** Settings ***
Library        SeleniumLibrary

*** Variables ***
${url}        https://opensource-demo.orangehrmlive.com/web/index.php/auth/login

${browser}        edge
${username}      Admin
${password}        admin123

*** Keywords ***
open Google
    Open Browser          ${url}       ${browser}

    Maximize Browser Window

orangehrm
    [Arguments]            ${username}          ${password}
    sleep                     5s
    Input Text          name=username      ${username}
    Input Text        name=password    ${password}
    sleep                      5s
    Capture Page Screenshot     filename=beforelogin.png
   Click Button         xpath://button[@type="submit"]
   sleep                     15s
    Capture Page Screenshot      filename=afterlogin.png
    Close Browser

*** Test Cases ***

test4_datadriven.robot
    open Google
    orangehrm      Admin    admin123