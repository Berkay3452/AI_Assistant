import os
from dotenv import load_dotenv
from settings import Settings

# .env dosyasını yükle
load_dotenv()

@classmethod
def validate_api_key(cls):
    """API anahtarının varlığını kontrol eder"""
    if not cls.HUGGINGFACE_API_KEY:
        raise ValueError(
            "HUGGINGFACE_API_KEY bulunamadı! "
            "Lütfen .env dosyasında API anahtarınızı tanımlayın."
        )
        
    if cls.HUGGINGFACE_API_KEY.strip() == "":
        raise ValueError(
            "HUGGINGFACE_API_KEY boş! "
            "Lütfen .env dosyasında geçerli bir API anahtarı tanımlayın."
        )
        
    return True
    
@classmethod
def get_headers(cls):
    """API çağrıları için header'ları döndürür"""
    cls.validate_api_key()
    return {
        "Authorization": f"Bearer {cls.HUGGINGFACE_API_KEY}",
        "Content-Type": "application/json"
    }
    
@classmethod
def is_exit_command(cls, text):
    """Verilen metnin çıkış komutu olup olmadığını kontrol eder"""
    if not text:
        return False
    return text.lower().strip() in cls.EXIT_COMMANDS


# Modül yüklendiğinde API anahtarını kontrol et
@classmethod
def api_key_control(cls):
    try:
        cls.validate_api_key()
        return "✅ Yapılandırma başarıyla yüklendi"
    except ValueError as e:
        return f"⚠️  Yapılandırma uyarısı: {e}"
