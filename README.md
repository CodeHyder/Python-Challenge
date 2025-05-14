# Python-Challenge
 
Este projeto é uma API RESTful construída com Django e Django REST Framework como parte de um desafio técnico.

## 🔧 Funcionalidades

- Criar posts
- Listar todos os posts
- Editar título e conteúdo de um post
- Deletar posts

## 🚀 Tecnologias

- Python 3.11
- Django 5.2.1
- Django REST Framework

## ▶️ Como rodar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/codeleap-api.git
   cd codeleap-api
   ```
2. Crie e ative o ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # ou venv\Scripts\activate no Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Execute as migrações e inicie o servidor:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

4. Acesse a API em:

   - Listar/Criar: http://127.0.0.1:8000/careers/
   - Atualizar/Deletar: http://127.0.0.1:8000/careers/<id>/
