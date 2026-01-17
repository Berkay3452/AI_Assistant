
# Çıkış komutlarını ayarlayan fonksiyon
def is_exit_command(text):
    exit_command = ["Görüşürüz", "bye", "Sonra Görüşürüz", "Güle Güle", "Kapat", "Çıkış"]
    return text.lower().strip() in exit_command




