from gtts import gTTS
import os

def Read(Text): 
    Text = str(Text)
    myobj = gTTS(text=Text, lang='en', slow=False)
    myobj.save("welcome.mp3")
    os.system("welcome.mp3")

PI = float(3.14)
Radius = float(input("Radius "))
Height = float(input("Height "))

RadiusSquared = Radius**float(2)
print(RadiusSquared)
print(2 * PI * RadiusSquared + (2 * PI * Radius * Height))