*** Settings ***

Library      SeleniumLibrary

*** Variables ***

${url}         https://opensource-demo.orangehrmlive.com/web/index.php/auth/login

${browser}        edge
${username}        Admin
${password}        admin123

*** Test Cases ***
test3_login.robot
    Open Browser         ${url}     ${browser}
    Wait Until Page Contains Element    name=username    10s
    Input Text        name = username  ${username}
    Input Text          name = password   ${password}
    sleep         5s
    Capture Page Screenshot      beforelogin.png
    Click Button         xpath://button[@type="submit"]
    sleep         10s
    Capture Page Screenshot         afterlogin.png
    Close Browser
