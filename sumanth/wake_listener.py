import speech_recognition as sr
import subprocess

recognizer = sr.Recognizer()

print("Listening for Jarvis...")

while True:
    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        text = recognizer.recognize_google(audio).lower()

        print("You said:", text)

        if "jarvis" in text:
            subprocess.Popen(
                r"C:\Users\linga\Downloads\Program files\Bujjamma\sumanth\dist\Bujjamma\Bujjamma.exe"
            )

    except Exception:
        pass