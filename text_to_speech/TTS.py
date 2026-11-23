from gtts import gTTS
print("Hello, this is a text to speech tool made with python")
text=input("Please, enter the text thal'll be turned to speech: ")
tts = gTTS (text=text, lang= 'en')
tts.save("speech.mp3")
print("Speech saved as speech.mp3")