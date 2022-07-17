import random
import time
import sys
import subprocess
import os
print("Champion picker. . .")

question = input("do you want to input new champs?(n/y)")
if question == ("y"):
    champions = input("champs: ").split()
    sex = open('champs.txt', 'w+')
    for champs in champions:
        sex.write("%s\n" % champs)
    print(random.choice(champions))
    time.sleep(30)
    subprocess.call([sys.executable, os.path.realpath(__file__)] +
                    sys.argv[1:])
if question ==("n"):
    a = open("champs.txt", "r")
    aa = a.readlines()
    print(random.choice(aa))
    print("have fun :)")
    time.sleep(5)
    subprocess.call([sys.executable, os.path.realpath(__file__)] +
                    sys.argv[1:])
else:
    print("invalid input.")
    subprocess.call([sys.executable, os.path.realpath(__file__)] +
                    sys.argv[1:])
time.sleep(30)

