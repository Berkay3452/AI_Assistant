from ses_alma import sesi_dinle
from cevap_verme import sesli_cevap
from model import cevap_olustur
from security import is_exit_command
import asyncio
import server

if __name__ == "__main__":

    # Jarvis Arayüz Sunucusunu Başlat
    print("🌐 Arayüz sunucusu başlatılıyor...")
    server.start()
    print("🤖 Asistan dinlemeye hazır...")

    try:
        while True:
            try:
                voice_input = sesi_dinle()
                if not voice_input:
                    continue

                if is_exit_command(voice_input):
                   print("Asistan: Görüşürüz efendim!")
                   break
                
                server.set_state("speaking")

                print("Kullanıcı: ", voice_input) # Kullanıcının söylediğini terminale yazdırıyor.
                voice_output = cevap_olustur(voice_input)  
                print("Asistan: ", voice_output) # Asistanın cevabını terminale yazdırıyor.
                sesli_cevap(voice_output) # Asistanın cevabını sesli olarak veriyor.

            except Exception as e:
                print(f"Bir hata oluştu: {e}")
                print("Devam ediliyor...")
                server.set_state("idle")
                continue
                
    except KeyboardInterrupt:
        print("\nProgram kapatılıyor...")
        server.set_state("idle")
    except Exception as e:
        print(f"Kritik hata: {e}")
        print("Program sonlandırılıyor.")
        server.set_state("idle")    