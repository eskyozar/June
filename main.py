import speech_recognition as spr
import pyttsx3
from time import strftime
import time
import webbrowser

engine = pyttsx3.init()

rate = 200

while True:
    # This is the Today's time


    r = spr.Recognizer()

    mc = spr.Microphone()

    # init

    with mc as source :
        print("Say 'Hello June' to speak")
        print("--------------------------")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        MyText = r.recognize_google(audio)
        MyText = MyText.lower()
        print(MyText)

    if 'hello june' in MyText :

        engine.say("Hi, How may I help you")
        engine.runAndWait()

        # Microphone
        with mc as source :
            print("Say something!")
            r.adjust_for_ambient_noise(source)
            audio1 = r.listen(source)
            my_text = r.recognize_google(audio1)
            my_text = my_text.lower()
            print(my_text)
        # Recognition
        """try:
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            # instead of `r.recognize_google(audio)`
            print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
        except spr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except spr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))"""

        if 'time' in my_text :
            # Today's time
            time = time.localtime()

            time = strftime("%I:%M:%p", time)

            # From here on is the code of the bot

            engine.getProperty('rate')
            engine.setProperty('rate', rate - 50)
            engine.say("Today's time is ")
            engine.say(time)
            print(time)
            engine.runAndWait()

            rate = 200

        elif "google" in my_text :

            engine.say("What do you want to search")
            engine.runAndWait()


            # Microphone
            with mc as source :
                print("What do you want to search")
                r.adjust_for_ambient_noise(source)
                audio2 = r.listen(source, phrase_time_limit=7)
                my_search = r.recognize_google(audio2)
                my_search = my_search.lower()
                print(my_search)
            # Recognition
            """try:
                # for testing purposes, we're just using the default API key
                # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
                # instead of `r.recognize_google(audio)`
                print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
            except spr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except spr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))"""

            try :
                from googlesearch import search
            except ImportError :
                print("No module named 'google' found")

            # to search
            query = my_search

            for j in search(query, tld="co.in", num=1, stop=1, pause=2) :
                print(j)

            url = j

            engine.getProperty('rate')
            engine.setProperty('rate', rate - 50)

            webbrowser.open_new_tab(url)

            engine.say("This is the search i found")
            engine.runAndWait()

            rate = 200

        elif 'bye' in my_text:

            engine.getProperty('rate')
            engine.setProperty('rate', rate - 50)
            engine.say("Goodbye")
            engine.say("Have a Nice day")
            engine.runAndWait()
            rate = 200
            break
        elif "date" in my_text:

            date = time.localtime()

            date = strftime("Today is %d of %B", date)

            engine.getProperty('rate')
            engine.setProperty('rate', rate - 50)
            engine.say(date)
            engine.runAndWait()


        else:
            engine.say("I don't understand")
            engine.runAndWait()
            rate = 200
