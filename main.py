from ses_alma import sesi_dinle
from cevap_verme import sesli_cevap
from model import cevap_olustur
from utils import is_exit_command
import asyncio

if __name__ == "__main__":
    try:
        while True:
            try:
                ses_input = sesi_dinle()
                
                # Hata mesajlarını kontrol et
                if (ses_input == "Anlayamadım, lütfen tekrar edin." or 
                    ses_input == "Ses algılanamadı, lütfen tekrar deneyin." or 
                    ses_input == "Bağlantı hatası! Google API'ye erişim sağlanamadı."):
                    print(ses_input)
                    continue

                if is_exit_command(ses_input):
                    print(f"Asistan: {ses_input}")
                    break
                
                print("Kullanıcı: ", ses_input)
                ses_output = cevap_olustur(ses_input)
                print("Asistan: ", ses_output)
                asyncio.run(sesli_cevap(ses_output))
                
            except Exception as e:
                print(f"Bir hata oluştu: {e}")
                print("Devam ediliyor...")
                continue
                
    except KeyboardInterrupt:
        print("\nProgram kapatılıyor...")
    except Exception as e:
        print(f"Kritik hata: {e}")
        print("Program sonlandırılıyor.")
            