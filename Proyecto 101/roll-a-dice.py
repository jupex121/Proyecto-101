import random

response = input("¿Quieres tirar el dado? Escribe 'yes' para sí o 'no' para no: ")

def roll(response):
    while response == "yes":
        no = random.randint(1,6)

        if(no == 1):
            print("[-----]")
            print("[     ]")
            print("[  0  ]")
            print("[     ]")
            print("[-----]")
        elif(no == 2):
            print("[-----]")
            print("[0    ]")
            print("[     ]")
            print("[    0]")
            print("[-----]")
        elif(no == 3):
            print("[-----]")
            print("[0    ]")
            print("[  0  ]")
            print("[    0]")
            print("[-----]")
        elif(no == 4):
            print("[-----]")
            print("[0   0]")
            print("[     ]")
            print("[0   0]")
            print("[-----]")
        elif(no == 5):
            print("[-----]")
            print("[0   0]")
            print("[  0  ]")
            print("[0   0]")
            print("[-----]")
        elif(no == 6):
            print("[-----]")
            print("[0   0]")
            print("[0   0]")
            print("[0   0]")
            print("[-----]")

        response = input("Quieres tirar el dado? Escribe 'y' para sí o 'n' para no: ")

    if(response == "no"):
        print("Thanks for playing!!")
    

roll(response)