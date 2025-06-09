# Calculadora Trabalhista

Uma aplicação web simples desenvolvida com **FastAPI** que calcula o valor estimado de uma rescisão trabalhista com base nos dados informados pelo usuário. A interface é feita com templates Jinja2 e estilizada com CSS para oferecer uma experiência amigável e responsiva.

---

## Funcionalidades

- Cálculo automático de:
  - Férias proporcionais
  - 13º salário proporcional
  - Aviso prévio (considerando motivo da saída)
  - Multa do FGTS (40%)
  - Saldo de salário (ainda fixo como 0 na versão atual)
- Formulário para entrada de dados: nome, salário mensal, meses trabalhados e motivo da saída
- Visualização clara dos valores calculados e total a receber
- Navegação simples entre página inicial, formulário e resultado

---

## Tecnologias Utilizadas

- Python 3.10+
- FastAPI
- Jinja2 Templates
- HTML5 / CSS3
- Uvicorn (servidor ASGI recomendado para rodar o app)

---

## Estrutura do Projeto

