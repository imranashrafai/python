print("======================== Text to Words ========================")
import win32com.client as ttw


speaker = ttw.Dispatch("SAPI.SpVoice")
te = []
showtouser = "Enter the elements to speak!"
speaker.Speak(showtouser)


while (items := input("Enter the elements!")) != "quit":
    te.append(items)

for i in range(len(te)):
    speaker.Speak(te[i])
    
    
    
speed = [99, 86, 87, 88, 111]
cars = ["Civic", "Honda", "Suzuki", "Prado", "Range Rover"]

# speaker has ability to learn string thats why integer converted to string
for i in range(len(cars)):
    speaker.Speak(cars[i] + " having speed" + str(speed[i]))
