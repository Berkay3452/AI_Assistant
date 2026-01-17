import os
from dotenv import load_dotenv

class Settings:
    """Sistem yapılandırma sınıfı"""
    
    # API Ayarları
    HUGGINGFACE_API_KEY = os.getenv('HUGGINGFACE_API_KEY')
    
    # Timeout Ayarları (saniye)
    SPEECH_TIMEOUT = int(os.getenv('SPEECH_TIMEOUT'))
    API_TIMEOUT = int(os.getenv('API_TIMEOUT'))
    TTS_TIMEOUT = int(os.getenv('TTS_TIMEOUT'))
    
    # Ses Ayarları
    SPEECH_LANGUAGE = os.getenv('SPEECH_LANGUAGE')
    TTS_VOICE = os.getenv('TTS_VOICE')
    
    # Model Ayarları
    LLM_MODEL = os.getenv('LLM_MODEL')
    
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
    
    @classmethod
    def get_all_settings(cls):
        """Tüm ayarları dict olarak döndürür (debug için)"""
        return {
            'speech_timeout': cls.SPEECH_TIMEOUT,
            'api_timeout': cls.API_TIMEOUT,
            'tts_timeout': cls.TTS_TIMEOUT,
            'speech_language': cls.SPEECH_LANGUAGE,
            'tts_voice': cls.TTS_VOICE,
            'llm_model': cls.LLM_MODEL,
            'api_key_exists': bool(cls.HUGGINGFACE_API_KEY),
            'exit_commands': cls.EXIT_COMMANDS
        }

# Modül yüklendiğinde API anahtarını kontrol et
try:
    Config.validate_api_key()
    print("✅ Yapılandırma başarıyla yüklendi")
except ValueError as e:
    print(f"⚠️  Yapılandırma uyarısı: {e}")