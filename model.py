import ollama # Offline LLM model kullanımı için
import re # Metin işleme için
from settings import Settings

def cevap_olustur(voice_input):

    try:
        response = ollama.chat(model=Settings.LLM_MODEL, messages=[
            {'role': 'user', 
             'content': voice_input}
        ])
        
        ham_cevap = response['message']['content']
        temiz_cevap = re.sub(r'<think>.*?</think>', '', ham_cevap, flags=re.DOTALL).strip()
        
        # Eğer temizlik sonrası boş kalırsa ham cevabı döndür
        if not temiz_cevap:
            return ham_cevap
        return temiz_cevap
    
    except Exception as e:
        print(f"Beklenmeyen hata: {e}")
        return "Üzgünüm, beklenmeyen bir hata oluştu. Lütfen tekrar deneyin."


