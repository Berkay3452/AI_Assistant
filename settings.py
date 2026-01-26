import os
from dotenv import load_dotenv

load_dotenv()
class Settings:
    """Sistem yapılandırma sınıfı"""

    # Model Ayarları
    LLM_MODEL = os.getenv('LLM_MODEL')

    EXIT_COMMANDS = [
        "görüşürüz",
        "bye",
        "asistanı kapat",
        "hoşçakal",
        "kapat"
    ]


