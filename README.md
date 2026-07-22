# 🚀 Testes de Automação - Hotmart Marketplace

Projeto acadêmico desenvolvido para a disciplina de **Teste de Software**, com o objetivo de automatizar cenários de testes funcionais da plataforma **Hotmart Marketplace** utilizando **Python** e **Selenium WebDriver**.

---

## 📖 Sobre o projeto

Este projeto contém scripts de automação responsáveis por validar funcionalidades importantes do fluxo de compra da plataforma Hotmart.

Os testes simulam ações reais de um usuário, como:

- Login na plataforma;
- Navegação pelo Marketplace;
- Seleção de cursos;
- Acesso ao checkout;
- Validação de formulários;
- Cenários de sucesso e falha durante a compra.

O objetivo foi aplicar conceitos de **Teste de Software**, garantindo a validação dos requisitos funcionais por meio de testes automatizados.

---

# 🧪 Casos de Teste

| Código | Descrição |
|---------|-----------|
| CT_006 | Acesso à funcionalidade de compra após login |
| CT_007 | Compra de curso com pagamento aprovado |
| CT_008 | Compra com cartão recusado |
| CT_009 | Tentativa de compra sem preencher dados obrigatórios |
| CT_010 | Compra utilizando e-mail inválido |

---

# 📂 Estrutura do Projeto

```text
testequalidade/
│
├── venv/
├── estoque.db
│
├── test_ct006_login.py
├── test_ct007_login.py
├── test_ct008_login.py
├── test_ct009_login.py
└── test_ct010_login.py
```

---

# ⚙ Tecnologias utilizadas

- Python 3
- Selenium WebDriver
- Google Chrome
- ChromeDriver
- SQLite
- VS Code

---

# ▶ Como executar

## 1. Clonar o projeto

```bash
git clone https://github.com/SEU-USUARIO/testequalidade.git
```

Entre na pasta:

```bash
cd testequalidade
```

---

## 2. Criar ambiente virtual

Windows

```bash
python -m venv venv
```

Ativar

```bash
venv\Scripts\activate
```

---

## 3. Instalar dependências

```bash
pip install selenium webdriver-manager
```

---

## 4. Executar um teste

Exemplo:

```bash
python test_ct006_login.py
```

ou

```bash
python test_ct007_login.py
```

---

# 📸 Evidências

## CT_006

- Login realizado com sucesso.
- Acesso ao Marketplace.
- Curso aberto automaticamente.
- Botão "Ir para o Carrinho" localizado.

---

## CT_007

Fluxo automatizado de compra contendo:

- Login
- Marketplace
- Seleção do curso
- Checkout
- Preenchimento dos dados
- Simulação de pagamento

---

## CT_008

Validação de cartão inválido.

Resultado esperado:

- Sistema bloquear pagamento;
- Exibir mensagem de erro.

---

## CT_009

Validação dos campos obrigatórios.

Resultado esperado:

- Campos destacados;
- Mensagens de erro;
- Compra bloqueada.

---

## CT_010

Validação de e-mail inválido.

Resultado esperado:

- Sistema impedir a continuidade da compra.

---

# 🎯 Objetivos alcançados

✔ Automatização de testes funcionais

✔ Utilização do Selenium WebDriver

✔ Interação com elementos dinâmicos

✔ Esperas explícitas (WebDriverWait)

✔ Localização de elementos por XPath e CSS Selector

✔ Validação de mensagens de erro

✔ Simulação de navegação de usuário real

✔ Estrutura organizada para manutenção dos testes

---

# 👨‍💻 Autor

**Davi Hudson Frazao**

Estudante de Engenharia de Software

GitHub:
https://github.com/davihudsonn

LinkedIn:
(adicione o link do seu LinkedIn)
