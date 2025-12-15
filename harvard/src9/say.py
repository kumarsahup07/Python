import cowsay
import pyttsx3

engine = pyttsx3.init()
this = input("What's this? ")
cowsay.cow(this) # type: ignore
engine.say(this)
engine.runAndWait()