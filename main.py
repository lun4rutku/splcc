# -*- coding: utf-8 -*-

from shell import metashell

print("""█▀ █▀█ █     █▀▀ █▀▀
▄█ █▀▀ █▄▄ ▄ █▄▄ █▄▄
""")

variables = {
    "module": None
}

while True:
    input = metashell.getUserInput()
    if (variables["module"]): module = variables["module"]
    else: module = None

    if (input.startswith("search")):
        
