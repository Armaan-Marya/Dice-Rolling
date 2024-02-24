from PIL import Image
import random

print("this is a Dice simulator: ")
x = "r"
while x == "r":
    number = random.randint(1,6)
    if number == 1:
        img = Image.open('DICE/face1.png')
        img.show()
    if number == 2:
        img = Image.open('DICE/face2.png')
        img.show()
    if number == 3:
        img = Image.open('DICE/face3.png')
        img.show()
    if number == 4:
        img = Image.open('DICE/face4.png')
        img.show()
    if number == 5:
        img = Image.open('DICE/face5.png')
        img.show()
    if number == 6:
        img = Image.open('DICE/face6.png')
        img.show()

    x = input("Enter r to roll the dice ")