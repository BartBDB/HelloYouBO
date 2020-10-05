from microbit import *
import speech
import random

arrayLengte = 3

onderwerp = ["He", "She", "Marco"]
werkwoord = ["runs", "learns", "plays"]
rest = ["at home", "at school", "at work"]

def sayWords1(word):
    print(word)
    speech.say(word, speed=100, pitch=100, throat=100, mouth=200)
    sleep(500)

def sayWords3(word):
    print(word)
    wordspeed = random.randint(10,200)
    wordpitch = random.randint(10,200)
    speech.say(word, speed=wordspeed, pitch=wordpitch, throat=100, mouth=200)
    print("Speed is: " + str(wordspeed))
    print("Pitch is: " + str(wordpitch))
    sleep(500)

def sayWords2():
    randomNumber = random.randint(0, arrayLengte - 1)
    print(randomNumber)
    display.show(randomNumber)
    sayWords3(onderwerp[randomNumber])
    randomNumber = random.randint(0, arrayLengte - 1)
    print(randomNumber)
    sayWords3(werkwoord[randomNumber])
    randomNumber = random.randint(0, arrayLengte - 1)
    print(randomNumber)
    sayWords3(rest[randomNumber])
    sleep(500)
    
while True:
    if button_a.is_pressed():
        sayWords1("Hello I am happy")
        display.show(Image.HAPPY)
    elif button_b.is_pressed():
        sayWords1("Why are you sad")
        display.show(Image.SAD)
    elif display.read_light_level() < 20:
        sayWords2()
    else:
        display.show(Image.SQUARE)