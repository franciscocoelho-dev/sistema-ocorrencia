# Sistema de Registro de Ocorrências Escolares

Sistema web desenvolvido em **Python** com o framework **Django** para registro, acompanhamento e gestão de ocorrências disciplinares e administrativas em ambiente escolar.

Projeto desenvolvido com os alunos do **2º ano do Curso Técnico em Desenvolvimento de Sistemas** do **CETI Liceu Parnaibano**, na disciplina de Programação.

---

## 📋 Sobre o Projeto

O sistema tem como objetivo digitalizar e organizar o processo de registro de ocorrências escolares (indisciplina, advertências, atrasos, entre outras), permitindo que gestores, coordenadores e professores registrem, consultem e acompanhem os casos de forma centralizada e segura.

### Funcionalidades

- [ ] Cadastro de alunos, turmas e funcionários
- [ ] Registro de ocorrências (tipo, descrição, data, envolvidos)
- [ ] Consulta e filtragem de ocorrências por aluno, turma ou período
- [ ] Controle de acesso por perfil de usuário (administrador, coordenador, professor)
- [ ] Geração de relatórios de ocorrências
- [ ] Histórico de ocorrências por aluno

---

## 🛠️ Tecnologias Utilizadas

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [SQLite](https://www.sqlite.org/) 
- HTML5, CSS3
- [Bootstrap](https://getbootstrap.com/)

---

## 🚀 Como Executar o Projeto

### Pré-requisitos

- Python 3.10 ou superior instalado
- pip (gerenciador de pacotes do Python)
- Git

### Passo a passo

1. Clone o repositório:
   ```bash
   git clone https://github.com/franciscocoelho-dev/sistema-ocorrencia
   cd sistema-ocorrencia
   ```

2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv

   # Windows
   venv\Scripts\activate

   # Linux/Mac
   source venv/bin/activate
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Aplique as migrações do banco de dados:
   ```bash
   python manage.py migrate
   ```

5. Crie um superusuário (para acessar o painel administrativo):
   ```bash
   python manage.py createsuperuser
   ```

6. Execute o servidor de desenvolvimento:
   ```bash
   python manage.py runserver
   ```

7. Acesse no navegador:
   ```
   http://127.0.0.1:8000/
   ```

---

## 📁 Estrutura do Projeto

```
nome-do-repositorio/
│
├── nome_do_projeto/       # Configurações principais do Django
├── ocorrencias/           # App responsável pelo registro de ocorrências
├── static/                # Arquivos estáticos (CSS, JS, imagens)
├── templates/             # Templates HTML
├── manage.py
├── requirements.txt
└── README.md
```
---

## 📄 Licença

Este projeto é de uso educacional, desenvolvido no âmbito da disciplina de Programação do CETI Liceu Parnaibano.

---

## 📌 Observações

Projeto em desenvolvimento como parte das atividades práticas da disciplina de Programação, com foco no aprendizado de desenvolvimento web com Django.