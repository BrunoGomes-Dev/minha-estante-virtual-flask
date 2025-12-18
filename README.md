# 📚 Minha Estante | Gerenciador de Leituras Pessoal

Este é um projeto prático que desenvolvi para aplicar meus estudos iniciais de **Python** e **Desenvolvimento Web**. O objetivo foi criar uma ferramenta simples onde eu pudesse registrar meus livros, escrever resenhas e organizar minha biblioteca pessoal de forma digital.

O foco aqui não foi apenas o visual, mas sim entender como os dados saem de um formulário e são salvos de forma organizada em um arquivo para serem lidos depois.

---

## 🛠️ O que foi usado

Escolhi ferramentas que me permitiram aprender a base de como a web funciona:

* **Python & Flask:** Usei para criar as rotas e a lógica do site.
* **Waitress:** Utilizado para rodar o servidor. É mais estável que o modo padrão de teste do Flask para manter o site rodando.
* **CSV para Armazenamento:** Em vez de um banco de dados complexo, usei o arquivo `books.csv` na raiz do projeto. Isso facilitou o aprendizado de manipulação de arquivos (leitura e escrita) com Python.
* **Jinja2:** Para não ter que repetir o mesmo código de cabeçalho e rodapé em todas as páginas, usei a herança de templates do Flask.

---

## ⚙️ Guia de Instalação

Se você quiser testar no seu computador:

    1. Clone o projeto:
       git clone https://github.com/seu-usuario/minha-estante.git
       cd minha-estante

    2. Instale as bibliotecas necessárias:
       pip install flask waitress

    3. Inicie o servidor:
       python app.py

    4. Acesso: 
       Abra o navegador em http://localhost:5000

---

## 🚀 Como funciona e Uso

* **Home:** Mostra todos os livros que estão salvos no seu arquivo `books.csv`.
* **Adicionar:** No botão `+`, você preenche o nome, autor, link de uma imagem e sua nota. Ao salvar, o Python adiciona uma nova linha no CSV e gera um ID automaticamente.
* **Detalhes:** Ao clicar em um livro, você é direcionado para uma página exclusiva para ler a resenha completa que escreveu.

---

## 📁 Estrutura de Pastas

```text
├── app.py              # Código principal com as rotas do site
├── books.csv           # Base de dados (Raiz do projeto)
├── static/             # Arquivos de estilo e ícones
│   ├── css/style.css
│   └── assets/image/logo-icon.svg
└── templates/          # As páginas HTML do site (Jinja2)
```
## Licensa

Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
