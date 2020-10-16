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
    except(FileExistsError, IsADirectoryError):
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

def c(project_name):
    try:
        os.mkdir(project_name)
    except(FileExistsError, IsADirectoryError):
        confirmation = input("Folder already exists, do you want to continue? (y/n)")
        if confirmation.lower() != 'y':
            exit()
    c = project_name + '/'
    main = open(f"{c}main.c", 'w')
    main.write(f'''#include <stdio.h>
int main() {{
    printf("{project_name}")
    return 0;
}}''')
def cpp(project_name):
    try:
        os.mkdir(project_name)
    except(FileExistsError, IsADirectoryError):
        confirmation = input("Folder already exists, do you want to continue? (y/n)")
        if confirmation.lower() != 'y':
            exit()
    cpp = project_name + '/'
    main = open(f"{cpp}main.cpp", 'w')
    main.write(f'''#include <iostream>
int main() {{
    std::cout << "{project_name}" << '\\n';
    return 0;
}}''')

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
        elif lang == 'c':
            c(project_name)
        elif lang == 'cpp':
            cpp(project_name)
