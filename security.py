from settings import Settings
 
def is_exit_command(text):
    """Verilen metnin çıkış komutu olup olmadığını kontrol eder"""
    if not text:
        return False
    return text.lower().strip() in Settings.EXIT_COMMANDS

def check_gitignore_security():
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

