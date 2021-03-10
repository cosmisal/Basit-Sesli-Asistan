import speech_recognition as sr
from datetime import datetime
import webbrowser, time, random, os
from gtts import gTTS
from playsound import playsound as ps


r = sr.Recognizer()

def record(ask = False):
    with sr.Microphone() as source:
        if ask:
            speak(ask)
            print(ask)
        audio = r.listen(source)
        voice = ''
        
        try:
            voice = r.recognize_google(audio, language='tr-tr')
            voice = voice.lower()
            
        except sr.UnknownValueError:
            speak("Seni anlayamadım ?")
            print("Seni anlayamadım ?")
            print(voice)
        except sr.RequestError:
            speak("Teknik bir sıkıntı var !")
            print("Teknik bir sıkıntı var !")
        return voice
    
def response(voice):
    if "ne yapıyorsun"  in voice:
        speak('şuan seni dinliyorum')
        print('şuan seni dinliyorum')
    if 'nasılsın' in voice:
        speak('iyiyim, sen nasılsın ?')
        print('iyiyim, sen nasılsın ?')
    if "saat kaç" in voice:
        speak(datetime.now().strftime("%H:%M:%S"))
        print("Saat: ", datetime.now().strftime("%H:%M:%S"))
    if "arama yap" in voice:
        search = record("ne aramak istersin ?")
        url = "https://www.google.com/search?q=" + search
        webbrowser.get().open(url)
        speak(search + "için bunları bulabildim")
        print(search + "için bunları bulabildim")
    if "çıkış" in voice:
        speak("İyi Günler")
        print("İyi Günler")
        exit()

def speak(string):
    tts = gTTS(string, lang='tr')
    rand = random.randint(1,9999)
    file = ('auido-'+str(rand)+'.mp3')
    tts.save(file)
    
    if ps(file):
        os.remove(file)
    else:
        os.remove(file)
        

print("Cosmisal Sizi Dinliyor")
speak("Cosmisal Sizi Dinliyor")

time.sleep(1)
while 1:
    voice= record()
    print(voice)
    response(voice)

    