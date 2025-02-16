# 🚀 PathSeeker - Um Fuzzer Simples para Diretórios e Arquivos

O **PathSeeker** é um fuzzer simples, mas eficiente, para encontrar diretórios e arquivos ocultos em aplicações web. Ele simula o comportamento de um atacante, testando caminhos com diferentes User-Agents.

---

## 📌 Funcionalidades

✅ Testa múltiplos diretórios rapidamente usando **Threads**  
✅ Alterna dinamicamente entre diferentes **User-Agents**  
✅ Salva os resultados em um arquivo **JSON formatado**  
✅ Suporte para **status codes relevantes** (200, 301, 403)  
✅ Fácil personalização da **Wordlist**  

---

## 📂 Estrutura do Projeto\

PathSeeker/ │── funcoes.py # Código principal do fuzzer │── main.py # Script de execução do programa │── wordlist.txt # Lista de diretórios e arquivos a serem testados │── requirements.txt # Dependências do projeto │── resultados/ # Pasta onde os arquivos JSON serão armazenados


🚀 Uso
✅Execute o fuzzer: python main.py
✅Digite a URL quando solicitado e o PathSeeker começará a busca.

📌 Exemplo de execução:

Digite a URL alvo: http://example.com
http://example.com/admin - Status: 200 - Tamanho 1328
http://example.com/uploads - Status: 403 - Tamanho 512
...
📊 Resultados
Os resultados são salvos em um arquivo JSON na pasta resultados/, por exemplo:

{
    "target": "http://example.com",
    "timestamp": "2025-02-16_15-40-26",
    "found_paths": [
        {
            "url": "http://example.com/admin",
            "status_code": 200,
            "content_length": 1328
        },
        {
            "url": "http://example.com/uploads",
            "status_code": 403,
            "content_length": 512
        }
    ]
}

🛠 Personalização
📝 Editar a Wordlist
A wordlist pode ser personalizada editando o arquivo wordlist.txt:

admin
login
uploads
backup.zip
config.php
Você pode adicionar ou remover caminhos conforme necessário.

📢 Contribuições
Sinta-se à vontade para contribuir!

Faça um Fork do projeto
Crie uma branch para suas alterações
Envie um Pull Request

⚠️ Aviso Legal
Este projeto deve ser utilizado apenas para fins educacionais e testes em ambientes autorizados. O uso indevido pode violar leis locais e resultar em penalidades.

Use com responsabilidade! 🚀
