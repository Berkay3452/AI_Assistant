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
                ses_input = sesi_dinle()
                if not ses_input:
                    continue

                # Hata mesajlarını kontrol et
                if (ses_input == "Anlayamadım, lütfen tekrar edin." or 
                    ses_input == "Ses algılanamadı, lütfen tekrar deneyin." or 
                    ses_input == "Bağlantı hatası! Google API'ye erişim sağlanamadı."):
                    print(ses_input)
                    continue

                if is_exit_command(ses_input):
                   print("Asistan: Görüşürüz efendim!")
                   break
                
                server.set_state("speaking")

                print("Kullanıcı: ", ses_input)
                ses_output = cevap_olustur(ses_input) 
                print("Asistan: ", ses_output) # Asistanın cevabını terminale yazdırıyor.
                asyncio.run(sesli_cevap(ses_output)) # Asistanın cevabını sesli olarak veriyor.

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