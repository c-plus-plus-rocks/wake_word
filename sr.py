import speech_recognition as sr
import webbrowser
import subprocess
import os
import math

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
                str = format(value)

                #hi, hey, hello, or yo
                #open browser
                # I love you
                #Where to dump bodies
                #What is... where is... why is...

                what = "what is" in str
                why = "why is" in str
                where = "where is" in str

                if str == "hi" or str == "hello" or str == "yo" or str == "hey":
                    print("Hey, How can I help you")

                if str == "open browser":
                    print("Opening Browser")
                    webbrowser.open_new_tab('google.com')

                if str == "open Notepad":
                    print("Opening Notepad")
                    subprocess.Popen('C:\WINDOWS\system32/notepad.exe')

                if str == "I love you":
                    print("I hate you")

                if str == "where to dump bodies":
                    print("In the dumpster behind your house")

                if what == True:
                    print("Searching...")
                    webbrowser.open_new_tab(str)

                if why == True:
                    print("Searching...")
                    webbrowser.open_new_tab(str)

                if where == True:
                    print("Searching")
                    webbrowser.open_new_tab(str)

                
        except sr.UnknownValueError:
            print("Oops! Didn't catch that")
        except sr.RequestError as e:
            print("Speech recognize failed {0}".format(e))
except KeyboardInterrupt:
    pass  
