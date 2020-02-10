*** Settings ***

Library  客户管理.py   WITH NAME  M

Library  客户管理.c2   WITH NAME  c2



*** Test Cases ***

管理员首页 - UI-0102

  c2.teststeps
