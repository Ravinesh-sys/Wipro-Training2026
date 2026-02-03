*** Settings ***
Library    BuiltIn

*** Variables ***
${USERNAME}    Rahul
@{COURSES}     Python    Selenium    RobotFramework

*** Test Cases ***
Display User Information
    Log    User name is ${USERNAME}
    Log To Console    Welcome ${USERNAME}

Display Course List
    Log    Available courses are ${COURSES}
    Log To Console    First course is ${COURSES}[0]
