import readline
import sys
import imp
from time import sleep

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def getUserInput(module):
    try:
        if module != None:
            return input(f"{bcolors.BOLD}{module}{bcolors.ENDC} - {bcolors.UNDERLINE}splcc{bcolors.ENDC} > ")
        elif module == None:
            return input(f"{bcolors.UNDERLINE}splcc{bcolors.ENDC} > ")
    except KeyboardInterrupt:
        print()
        for x in range(1,9):
            for i in ("⠻", "⠽", "⠾", "⠷", "⠯", "⠟"):
                sleep(0.1)
                if x == 8:
                    sys.exit("Bye Bye!")
                    break
                else:
                    print('Exiting... ' +i, end = '\r')