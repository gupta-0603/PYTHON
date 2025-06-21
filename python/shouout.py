import pyttsx3
speaker = pyttsx3.init()
l = ['aditya', 'larry', 'carry']
for names in l:
        speaker.say(f'Shout out to {names}')
        speaker.say("hello my name is aditya")
        speaker.runAndWait()
        speaker.say("you are smart")