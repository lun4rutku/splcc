# -*- coding: utf-8 -*-

from shell import metashell
import imp
from time import sleep

def clear():
    print("\x1B[2J")

clear()

print("""█▀ █▀█ █     █▀▀ █▀▀
▄█ █▀▀ █▄▄ ▄ █▄▄ █▄▄
""")

variables = {
    "module": None
}

global sets

sets = {}

phonemd = {
    "supported": [
        "+90"
    ]
    "typeofatttacks": [
        "smsbomber"
    ]
}

while True:
    inputtext = metashell.getUserInput(variables["module"])
    if (variables["module"]): module = variables["module"]
    else: module = None

    if (inputtext.startswith("search ")):
        splittedinput = inputtext.split()
        if splittedinput[1] == "phone":
            print("Searching for country code is supported.")
            for x in range(1,10):
                for i in ("⠻", "⠽", "⠾", "⠷", "⠯", "⠟"):
                    sleep(0.1)
                    if x == 10:
                        break
                    else:
                        print('Checking. ' +i, end = '\r')
            for eachSplit in splittedinput:
                if eachSplit.startswith("country->"):
                    countrycode = eachSplit.split("country->")[1]
                else:
                    countrycode = None
                if eachSplit.startswith("number->"):
                    phonenumber = eachSplit.split("number->")[1]
                else:
                    phonenumber = None
            if (countrycode!=None) and (countrycode in phonemd["supported"]):
                print("Supported country code.")
            elif not (countrycode!=None):
                print("Not entered country code for scan.")
            elif (countrycode!=None) and not (countrycode in phonemd["supported"]):
                print("Unsupported country code.")
            else:
                print("if -> countrycode(isnotnone) and supported(countrycode): result(FALSE)")
    elif (inputtext.startswith("use ")):
        splittedinput = inputtext.split()
        if splittedinput[1] == "phone":
            sets = {}
            print("Using module phone.")
            variables["module"] = "phone"
    elif (inputtext.startswith("set ")):
        if variables["module"] == "phone":
            splittedinput = inputtext.split()
            for eachSplit in splittedinput:
                    if eachSplit.startswith("country->"):
                        sets["countrycode"] = eachSplit.split("country->")[1]
                        print(f"country -> {sets['countrycode']}")
                    if eachSplit.startswith("number->"):
                        sets["phonenumber"] = eachSplit.split("number->")[1]
                        print(f"number -> {sets['phonenumber']}")
    elif (inputtext.startswith("unset")):
        sets = {}
    elif (inputtext.startswith("deuse")):
        variables["module"] = None
    elif (inputtext.startswith("start")):
        startattack=False
        if splittedinput[1] == "phone":
            try:
                if(sets["countrycode"] != None or sets["phonenumber"] != None):
                    startattack=True
            except:
                print("Enter sets.")
            if startattack:
                smsbomber(sets["phonenumber"])
    elif (inputtext.startswith("clear")):
        clear()
        print("""█▀ █▀█ █     █▀▀ █▀▀
▄█ █▀▀ █▄▄ ▄ █▄▄ █▄▄
""")