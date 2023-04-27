# -*- coding: utf-8 -*-

from shell import metashell

print("""█▀ █▀█ █     █▀▀ █▀▀
▄█ █▀▀ █▄▄ ▄ █▄▄ █▄▄
""")

variables = {
    "module": None
}

phonemd = {
    "supported": [
        "+90"
    ]
}

while True:
    input = metashell.getUserInput()
    if (variables["module"]): module = variables["module"]
    else: module = None

    if (input.startswith("search ")):
        splittedinput = input.split()
        if splittedinput[1] == "phone":
            print("Searching for country code is supported.")
            countrycode = splittedinput[2].split("--")[1]
            if countrycode in phonemd["supported"]:
                print("Supported country code.")
                