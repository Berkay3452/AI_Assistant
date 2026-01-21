import os
from settings import Settings
from security import validate_api_key

def cevap_olustur(ses_input):
    
    try:
        # API anahtarı güvenlik kontrolü
        if not validate_api_key():
            raise ValueError("API anahtarı güvenlik kontrolü başarısız")
        
        payload = {
            "messages": [
                {
                    "role": "user",
                    "content": ses_input  
                }
            ],
            
            "model": Settings.LLM_MODEL
        }   
        
    except ValueError as e:
        # API anahtarı veya yapılandırma hatası
        error_msg = str(e)
        print(f"Yapılandırma hatası: {error_msg}")
        
        # API anahtarı ile ilgili hatalar için özel mesaj
        if "API anahtarı" in error_msg or "HUGGINGFACE_API_KEY" in error_msg:
            return (
                "🔑 API anahtarı sorunu tespit edildi. "
                "Sistem yöneticinizle iletişime geçerek API anahtarının doğru "
                "şekilde yapılandırıldığından emin olun."
            )
        else:
            return "Üzgünüm, sistem yapılandırmasında bir sorun var. Lütfen yöneticinizle iletişime geçin."
        
    except Exception as e:
        print(f"Beklenmeyen hata: {e}")
        return "Üzgünüm, beklenmeyen bir hata oluştu. Lütfen tekrar deneyin."


