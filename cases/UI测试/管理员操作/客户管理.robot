*** Settings ***

Library  客户管理.py   WITH NAME  M

Library  客户管理.c2   WITH NAME  c2

Library  客户管理.c3   WITH NAME  c3



*** Test Cases ***

管理员首页 - UI-0102

  c2.teststeps


管理员首页 - UI-0103

  c3.teststeps
