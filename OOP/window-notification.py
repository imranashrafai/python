from plyer import notification
import win32com.client as ttw
import time


speaker = ttw.Dispatch("SAPI.SpVoice")


timetorun = 3


time.sleep(timetorun)
message = "Hey Imran,It's time to drink water!"


notification.notify(
    title="Reminder",
    message="It's time to drink water!",
    timeout=10,
)
speaker.Speak(message)
