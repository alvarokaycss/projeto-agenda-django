# Projeto Agenda

Este projeto é uma aplicação web de agenda desenvolvida como parte do curso "Python do Início ao Avançado" do Luiz Otávio Miranda. Ele permite gerenciar contatos e usuários, com funcionalidades como criação, edição, visualização e exclusão de entradas.

---

## 🚀 Tecnologias Utilizadas

O projeto foi construído utilizando as seguintes **tecnologias** e **conceitos**:

* **Python**: Linguagem de programação principal.
* **Django**: Framework web de alto nível para o desenvolvimento rápido e seguro.
* **HTML**: Para a estruturação das páginas web.
* **CSS**: Para a estilização e design da interface do usuário.
* **SQL**: Para o gerenciamento e persistência dos dados (banco de dados).

---

## ✨ Funcionalidades Principais

* **Autenticação de Usuários**:
    * Criação de novas contas de usuário.
    * Login e logout.
* **Gerenciamento de Contatos**:
    * Adicionar novos contatos (nome, sobrenome, telefone, email, data de criação, descrição, categoria).
    * Visualizar detalhes dos contatos.
    * Editar informações de contatos existentes.
    * Excluir contatos.
* **Validações e Tratamento de Erros**:
    * Garantia da integridade dos dados através de validações nos formulários.
    * Tratamento de possíveis erros para uma experiência de usuário mais robusta.
* **Código Dinâmico**:
    * Lógicas de verificação e renderização condicional para uma interface mais interativa.

---

## 🛠️ Como Rodar o Projeto Localmente

Para rodar este projeto em sua máquina local, siga os passos abaixo:

1.  **Clone o Repositório:**
    ```bash
    git clone [https://github.com/SeuUsuario/NomeDoSeuRepositorio.git](https://github.com/SeuUsuario/NomeDoSeuRepositorio.git)
    cd NomeDoSeuRepositorio
    ```
    *Lembre-se de substituir `SeuUsuario` e `NomeDoSeuRepositorio` pelos seus dados do GitHub.*

2.  **Crie e Ative um Ambiente Virtual (Recomendado):**
    ```bash
    python -m venv venv
    # No Windows
    .\venv\Scripts\activate
    # No macOS/Linux
    source venv/bin/activate
    ```

3.  **Instale as Dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute as Migrações do Banco de Dados:**
    ```bash
    python manage.py migrate
    ```

5.  **Crie um Superusuário (Opcional, para acessar o admin do Django):**
    ```bash
    python manage.py createsuperuser
    ```
    *Siga as instruções no terminal para criar seu usuário e senha.*

6.  **Inicie o Servidor de Desenvolvimento:**
    ```bash
    python manage.py runserver
    ```

Agora você pode acessar a aplicação em seu navegador através do endereço `http://127.0.0.1:8000/`.

---

## ☁️ Próximos Passos (Deploy)

Atualmente, o projeto está disponível apenas localmente e no GitHub. O próximo objetivo é aprender e realizar o **primeiro deploy** desta aplicação, tornando-a acessível publicamente na web. Estou pesquisando e estudando as melhores práticas para isso.

---

## 🤝 Contribuições

Este projeto foi desenvolvido com propósitos de aprendizado. Contribuições são bem-vindas! Sinta-se à vontade para abrir [issues](https://github.com/SeuUsuario/NomeDoSeuRepositorio/issues) ou [pull requests](https://github.com/SeuUsuario/NomeDoSeuRepositorio/pulls).

---

## 📜 Licença

Este projeto está licenciado sob a licença [MIT](https://opensource.org/licenses/MIT).

---

## 📧 Contato

Para qualquer dúvida ou sugestão, entre em contato:

* **Nome:** Álvaro Kayc da Silva Santos
* **Email:** kayycsantos@gmail.com
* **LinkedIn:** alvarokaycss (https://www.linkedin.com/in/alvarokaycss/)

---
