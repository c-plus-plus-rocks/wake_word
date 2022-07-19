import speech_recognition as sr
import webbrowser
import subprocess

r = sr.Recognizer()
m = sr.Microphone()

try:
    print("A moment of silence, please...")
    with m as source: r.adjust_for_ambient_noise(source)
    print("Set minimum energy threshold to {}".format(r.energy_threshold))
    while True:
        with m as source: audio = r.listen(source)
        try:
            # recognize speech using Google Speech Recognition
            value = r.recognize_google(audio)

            # we need some special handling here to correctly print unicode characters to standard output
            if str is bytes:  # this version of Python uses bytes for strings (Python 2)
                print(format(value).encode("utf-8"))
            else:  # this version of Python uses unicode for strings (Python 3+)
                print(format(value))
                if format(value) == "hi":
                    print("Hey, How can I help you")
                if format(value) == "open browser":
                    print("Opening Browser")
                    webbrowser.open_new_tab('google.com')
                if format(value) == "open Notepad":
                    print("Opening Notepad")
                    subprocess.Popen('C:\WINDOWS\system32/notepad.exe')
                if format(value) == "open visual studio":
                    subprocess.Popen('C:\Users\youthprograms2022\AppData\Local\Programs\Microsoft VS Code')
                if format(value) != "open Notepad" or "open browser":
                    print("Sorry, I don't understand")
        except sr.UnknownValueError:
            print("Oops! Didn't catch that")
        except sr.RequestError as e:
            print("Speech recognize failed {0}".format(e))
except KeyboardInterrupt:
    pass  