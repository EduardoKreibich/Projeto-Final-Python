```markdown
# M5 - Projeto Final Kanvas

## Descrição

O projeto "M5 - Projeto Final Kanvas" é uma aplicação desenvolvida como trabalho final do Módulo 5 do bootcamp FullStack na Kenzie Academy Brasil. Trata-se de uma API para gerenciamento de cursos e aulas de uma escola na modalidade de Ensino a Distância (EAD). Utilizando Python com Django e Django Rest Framework, a aplicação permite a criação de usuários (estudantes ou superusuários), autenticação via JSON Web Token (JWT), criação e listagem de cursos, onde estudantes visualizam apenas os cursos nos quais estão matriculados. O projeto utiliza PostgreSQL como banco de dados e inclui documentação com Swagger.

## Pré-requisitos

Antes de iniciar, certifique-se de ter os seguintes pacotes instalados globalmente em seu sistema:

- `pytest`
- `pytest-testdox`
- `pytest-django`

Você pode verificar se eles estão instalados executando:

```bash
pip list
```

Se os pacotes aparecerem na listagem, desinstale-os com:

```bash
pip uninstall pytest pytest-testdox pytest-django -y
```

## Configuração do Ambiente

1. **Crie um ambiente virtual:**

   ```bash
   python -m venv venv
   ```

2. **Ative o ambiente virtual:**

   - **Linux e Mac:**

     ```bash
     source venv/bin/activate
     ```

   - **Windows (PowerShell):**

     ```bash
     .\venv\Scripts\activate
     ```

   - **Windows (GitBash):**

     ```bash
     source venv/Scripts/activate
     ```

3. **Instale as dependências necessárias:**

   ```bash
   pip install model_bakery pytest-testdox pytest-django
   ```

## Execução dos Testes

Para rodar a bateria de testes, utilize o comando:

```bash
pytest --testdox -vvs
```

## Estrutura do Projeto

A estrutura de diretórios do projeto é a seguinte:

```
Projeto-Final-Python/
├── _core/
├── accounts/
├── contents/
├── courses/
├── students_courses/
├── tests/
├── .env.example
├── .gitignore
├── README.md
├── build.sh
├── manage.py
├── pytest.ini
└── requirements.txt
```

## Configuração do Ambiente

1. **Crie um arquivo `.env`** na raiz do projeto baseado no arquivo `.env.example` fornecido. Este arquivo deve conter as variáveis de ambiente necessárias para a configuração da aplicação.

2. **Instale as dependências do projeto:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Execute as migrações do banco de dados:**

   ```bash
   python manage.py migrate
   ```

4. **Inicie o servidor de desenvolvimento:**

   ```bash
   python manage.py runserver
   ```

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.
