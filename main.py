from funcoes import *

if __name__ == "__main__":
    url_alvo = input("Digite a URL alvo: ").strip()
    wordlist = wordlist_base = [
    "admin", "login", "dashboard", "config", "db", "user", "home", "index", "private", "uploads",
    "test", "settings", "files", "img", "assets", "css", "js", "docs", "backup", "download", "admin123", "test123", "root", "manager", "uploads", "configurations", "adminpanel", "cms", 
    "phpmyadmin", "login2", "backup", "files", "secure", "v1", "v2", "panel", "uploads", "logs"
]
    fuzzer(url_alvo,wordlist)
