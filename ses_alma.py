import vosk
import sys
import os
import pyaudio
import json

VOSK_MODEL_PATH = "vosk-model-small-tr-0.3"  # Türkçe model

# Model Kontrolü
if not os.path.exists(VOSK_MODEL_PATH):
    print(f"HATA: '{VOSK_MODEL_PATH}' klasörü bulunamadı!")
    sys.exit(1)
    
vosk.SetLogLevel(-1)
print("🎤 Yerel Ses Motoru (Vosk) Hazırlanıyor...")

try: 
    model = vosk.Model(VOSK_MODEL_PATH)
    rec = vosk.KaldiRecognizer(model, 16000)

except Exception as e:
    print(f"HATA: Vosk modeli yüklenemedi: {e}")
    sys.exit(1)

def sesi_dinle():
    p = pyaudio.PyAudio()

    # Varsayılan mikrofonu (Laptop Mic) kullanır
    stream = p.open(format=pyaudio.paInt16, 
                    channels=1, 
                    rate=16000, 
                    input=True, 
                    frames_per_buffer=8000)
    
    stream.start_stream()

    try:
        while True:
            # Mikrofondan veri okuyacak
            data = stream.read(4000, exception_on_overflow=False)
            
            # Vosk sesi analiz etsin
            if rec.AcceptWaveform(data):
                sonuc = json.loads(rec.Result())
                temiz_metin = sonuc['text']
                
                # Eğer anlamlı bir cümle yakaladıysa
                if temiz_metin:
                    # Akışı temizce kapat
                    stream.stop_stream()
                    stream.close()
                    p.terminate()
                    return temiz_metin
                    
    except Exception as e:
        print(f"Ses alma hatası: {e}")
        return ""
