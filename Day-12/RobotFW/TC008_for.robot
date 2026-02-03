*** Test Cases ***
Print Names
    FOR    ${name}    IN    Ram    Ravi    Taj
        Log To Console    ${name}
    END

*** Test Cases ***
FOR Loop Range
    FOR    ${i}    IN RANGE    1    6
        Log  NUMBER:${i}
       
    END

*** Test Cases ***
FOR Loop With Step
    FOR    ${i}    IN RANGE  0  10  2
      Log  Value:${i}
   END


*** Test Cases ***
FOR Loop Enumerate
    FOR   ${index}    ${value}    IN ENUMERATE a  b  c

    Log  ${index}=${value}
   END
