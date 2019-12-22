


*** Settings ***
Library                     BlogSeleniumLibrary
Suite Teardown              CLOSE BROWSER

*** Variables ***
${platform}          WINDOWS
${browser}            chrome
${version}            79
${remote_url}         http://192.168.63.1:4444/wd/hub
${login_url}          https://account.cnblogs.com/signin


*** Test Cases ***
登录-XXXXXX
    登录-打开浏览器并进入登录页面


*** Keywords ***
登录-打开浏览器并进入登录页面
    ${options}=  GET CHROME OPTIONS  D:/projectname/testdata/downloads   #这里是写死的路径，实际项目中应该动态去获取工程路径/testdata/downloads
    OPEN BROWSER NEW  platform=${platform}  browserName=${browser}  version=${version}
                      ...  chrome_options=${options}  remote_url=${remote_url}
    GO TO  ${login_url}
    SET SELENIUM IMPLICIT WAIT  10
    MAXIMIZE BROWSER WINDOW
