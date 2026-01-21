import os
from dotenv import load_dotenv

load_dotenv()
class Settings:
    """Sistem yapılandırma sınıfı"""
    
    # API Ayarları
    HUGGINGFACE_API_KEY = os.getenv('HUGGINGFACE_API_KEY')
    
    # Timeout Ayarları (saniye)
    SPEECH_TIMEOUT = os.getenv('SPEECH_TIMEOUT')
    API_TIMEOUT = os.getenv('API_TIMEOUT')
    TTS_TIMEOUT = os.getenv('TTS_TIMEOUT')
    
    # Ses Ayarları
    SPEECH_LANGUAGE = os.getenv('SPEECH_LANGUAGE')
    TTS_VOICE = os.getenv('TTS_VOICE')
    
    # Model Ayarları
    LLM_MODEL = os.getenv('LLM_MODEL')

    EXIT_COMMANDS = [
        "görüşürüz",
        "bye",
        "asistanı kapat",
        "hoşçakal",
        "kapat"
    ]


