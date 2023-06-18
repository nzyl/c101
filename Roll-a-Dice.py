import random

response = "y"

while response == "y":
    no = random.randint(1, 6)
    if no == 1:
        print("\n[-----]")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("[-----]\n")
    elif no == 2:
        print("\n[-----]")
        print("[ 0   ]")
        print("[     ]")
        print("[   0 ]")
        print("[-----]\n")
    elif no == 3:
        print("\n[-----]")
        print("[     ]")
        print("[0 0 0]")
        print("[     ]")
        print("[-----]\n")
    elif no == 4:
        print("\n[-----]")
        print("[0   0]")
        print("[     ]")
        print("[0   0]")
        print("[-----]\n")
    elif no == 5:
        print("\n[-----]")
        print("[0   0]")
        print("[  0  ]")
        print("[0   0]")
        print("[-----]\n")
    else:
        print("\n[-----]")
        print("[0 0 0]")
        print("[     ]")
        print("[0 0 0]")
        print("[-----]\n")

    response = input("Enter y to roll again and n to exit:")
