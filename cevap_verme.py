import edge_tts
import tempfile
import os 
from playsound import playsound

async def sesli_cevap(ses_output):
    try:
        if ses_output:
            communicate = edge_tts.Communicate(text=ses_output, voice="tr-TR-AhmetNeural")
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp:
               temp_file = temp.name
            await communicate.save(temp_file)
            playsound(temp_file)
        else:
            print("Sesli cevap için geçerli bir çıktı sağlanmadı.")        
    except Exception as e:
        print(f"Sesli cevap verme hatası: {e}")   
    finally:
        if os.path.exists(temp_file):
            try:
                os.remove(temp_file)     
            except Exception as e:
                print(f"Dosya silinemedi: {e}")

