import os
from settings import Settings

def _validate_api_key_security():
    """
    API anahtarı güvenlik kontrollerini yapar
    
    Returns:
        bool: Güvenlik kontrolleri başarılıysa True
        
    Raises:
        ValueError: Güvenlik kontrolü başarısızsa açıklayıcı hata mesajı ile
    """
    try:
        # 1. API anahtarının environment variable'dan okunduğunu kontrol et
        api_key = os.getenv('HUGGINGFACE_API_KEY')
        
        # 2. .env dosyasının .gitignore'da olduğunu kontrol et
        _check_gitignore_security()
        
        return True
        
    except Exception as e:
        # Beklenmeyen hatalar için genel mesaj
        raise ValueError(
            f"❌ API anahtarı güvenlik kontrolü sırasında hata oluştu: {str(e)}\n"
            "Çözüm: .env dosyasını kontrol edin ve geçerli bir API anahtarı tanımlayın."
        )

def _check_gitignore_security():
    """
    .env dosyasının .gitignore'da olduğunu kontrol eder (güvenlik)
    
    Raises:
        ValueError: .env dosyası .gitignore'da değilse
    """
    try:
        gitignore_path = '.gitignore'
        
        # .gitignore dosyası var mı kontrol et
        if not os.path.exists(gitignore_path):
            raise ValueError(
                "⚠️  Güvenlik uyarısı: .gitignore dosyası bulunamadı!\n"
                "Çözüm: .gitignore dosyası oluşturun ve '.env' ekleyin."
            )
        
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

def cevap_olustur(ses_input):
    
    try:
        # API anahtarı güvenlik kontrolü
        if not _validate_api_key_security():
            raise ValueError("API anahtarı güvenlik kontrolü başarısız")
        
        # API anahtarını kontrol et ve header'ları al
        headers = Settings.get_headers()
        
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


