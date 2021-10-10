#!/usr/bin/env python3
#! /usr/bin/python3
# -*- coding: cp1251 -*-
import cgi
import os
from http import cookies

form = cgi.FieldStorage()
name = form.getfirst("name", "не задано")
lastname = form.getfirst("lastname", "не задано")
checkboxes = form.getlist("checkbox")
if "не задано" in checkboxes:
    checkboxes.remove("не задано")
operationSystem = form.getfirst("OS", "не задано")
stringCheckbox = ""
if len(checkboxes) == 0:
    stringCheckbox = "не задано"
else:
    for i in checkboxes:
        stringCheckbox += i + " " 
checkboxes.clear()

cookie = cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
cookie = cookie.get("count")
if cookie is None:
    print(f"Set-cookie: count={1}");
    count = 1
else:
    count = int(cookie.value) + 1
    print(f"Set-cookie: count={count}")

print("Content-type: text/html\n") 
print(f'''
<html>
    <head>
        <title>Анкета</title>
        <meta charset = 'cp1251'>
    </head>
    <body style = 'text-align: center'>
        <div style = "background-color: red; color: yellow; width: 60%; margin-left: calc(20% - 5px);padding: 5px">
            <h3>Отримана анкета програміста</h3>
            <p>Ім'я користувача: {name}</p>
            <p>Прізвище користувача: {lastname} </p>
            <p>Якими мовами програмування ви володієте? - {stringCheckbox} </p>
            <p>Якій операційні системі ви надаєте перевагу? - {operationSystem}</p>
        </div>
        <p style = "text-align: center;">Кількість звернень: {count} </p>
    </body>
</html>
''')
