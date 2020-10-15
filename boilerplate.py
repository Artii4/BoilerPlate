#!/usr/bin/env python3

import sys
import os

langs = [
    'html', 'c', 'cpp'
]


def isIn(item, array):
    for i in array:
        if item == i:
            return True
    return False


def html(project_name):
    try:
        os.mkdir(project_name)
    except(FileExistsError):
        confirmation = input("Folder already exists, do you want to continue? (y/n)")
        if confirmation.lower() != 'y':
            exit()
    folder = project_name + '/'
    html = f"{folder}index.html"
    css = f"{folder}style.css"
    js = f"{folder}index.js"

    index = open(html, 'w+')
    index.write(f'''<!DOCTYPE html>
<html>
    <head>
        <link rel="stylesheet" href="style.css">
        <meta charset="UTF-8">
        <title>{project_name}</title>
    </head>
    <body>
        <h1>{project_name}</h1>
        <script href="index.js"></script>
    </body>
</html>''')
    stylesheet = open(css, "w")
    script = open(js, "w")


if len(sys.argv) == 1:
    print("Expected argument")
else:
    lang = str(sys.argv[1].lower())
    if isIn(lang, langs):
        project_name = input("How would you like to name your project? ")
        confirmation = input("Are you sure? (y/n) ")
        if confirmation.lower() != 'y':
            exit()

        if lang == "html":
            html(project_name)
            print("Project made!")
