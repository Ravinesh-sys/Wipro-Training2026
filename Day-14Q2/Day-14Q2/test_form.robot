* Settings *
Library    SeleniumLibrary

Suite Setup       Open Test Browser
Suite Teardown    Close Browser
Test Teardown     Capture Page Screenshot

* Variables *
${URL}        https://demoqa.com/automation-practice-form
${BROWSER}    edge

* Test Cases *
Submit Practice Form
    [Tags]    smoke    formtest


    Execute JavaScript    document.querySelectorAll("iframe").forEach(el => el.remove());


    Input Text    id=firstName    Ravinesh
    Input Text    id=lastName     Tiwari
    Input Text    id=userEmail    ravinesh@test.com


    Scroll Element Into View    xpath=//label[text()='Male']
    Sleep    1
    Execute JavaScript    document.querySelector("label[for='gender-radio-1']").click()


    Input Text    id=userNumber    8948965454


    Execute JavaScript    document.querySelector("label[for='hobbies-checkbox-1']").click()


    Execute JavaScript    window.scrollTo(0, document.body.scrollHeight)
    Sleep    1


    Click Element    id=state
    Click Element    xpath=//div[text()='NCR']

    Sleep    2


    Execute JavaScript    document.getElementById("submit").click()

    Sleep    2


    ${modal_title}=    Get Text    id=example-modal-sizes-title-lg
    Should Be Equal    ${modal_title}    Thanks for submitting the form


    Run Keyword If    '${modal_title}' == 'Thanks for submitting the form'    Log To Console    Form Submitted Successfully

* Keywords *
Open Test Browser
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window