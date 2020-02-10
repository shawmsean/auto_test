*** Settings ***

Library  药品管理.py   WITH NAME  M

Library  药品管理.c2   WITH NAME  c2



*** Test Cases ***

药品管理 - UI-0103

  c2.teststeps
