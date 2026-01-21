import speech_recognition as sr

def sesi_dinle():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            audio = r.listen(source, timeout=2) #timeout ile ses almayı bekleme süresi belirleniyor.
            voice = r.recognize_google(audio, language="tr-TR") #voice = komut temsil ediyor 
            return voice

        except sr.WaitTimeoutError:
            return "Ses algılanamadı, lütfen tekrar deneyin."

        except sr.UnknownValueError:
            return "Anlayamadım, lütfen tekrar edin."
            
        except sr.RequestError:
            return "Bağlantı hatası! Google API'ye erişim sağlanamadı."


      