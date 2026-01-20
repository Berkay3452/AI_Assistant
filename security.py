from settings import Settings

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


def _check_gitignore_security():
    """
    .env dosyasının .gitignore'da olduğunu kontrol eder (güvenlik)
    
    Raises:
        ValueError: .env dosyası .gitignore'da değilse
    """

    gitignore_path = '.gitignore'

    try:
        # .gitignore içeriğini oku
        with open(gitignore_path, 'r', encoding='utf-8') as f:
            gitignore_content = f.read()
        
        # .env dosyasının ignore edilip edilmediğini kontrol et
        if '.env' not in gitignore_content:
            raise ValueError(
                "⚠️  Güvenlik uyarısı: .env dosyası .gitignore'da değil!\n"
                "Çözüm: .gitignore dosyasına '.env' satırını ekleyin."
            )  
    except FileNotFoundError:
        raise ValueError(
            "⚠️  Güvenlik uyarısı: .gitignore dosyası okunamadı!\n"
            "Çözüm: .gitignore dosyasının var olduğundan ve okunabilir olduğundan emin olun."
        )
    except Exception as e:
        # Bu kritik bir güvenlik kontrolü değil, uyarı olarak geç
        print(f"⚠️  .gitignore güvenlik kontrolü atlandı: {e}")

