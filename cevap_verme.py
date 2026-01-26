import pyttsx3

engine = pyttsx3.init()

# Hız: 150-170 arası idealdir. (Daha hızlı istersen artır)
engine.setProperty('rate', 160)

# Ses Seviyesi (0.0 ile 1.0 arası)
engine.setProperty('volume', 1.0)

# Türkçe Sesi Ayarla
voices = engine.getProperty('voices')
voice_found = False

for voice in voices:
    # Bilgisayarındaki Türkçe sesi bulmaya çalışır
    if "Turkish" in voice.name or "TR" in voice.id or "Microsoft Tolga" in voice.name:
        engine.setProperty('voice', voice.id)
        voice_found = True
        break

if not voice_found:
    print("Uyarı: Türkçe ses paketi bulunamadı, varsayılan ses kullanılacak.")

def sesli_cevap(voice_output):
    try:
        engine.say(voice_output)
        engine.runAndWait()

    except Exception as e:
        print(f"Sesli cevap hatası: {e}")

