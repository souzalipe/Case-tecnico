# Case Técnico – Classificação de Emails

## Visão Geral

Este projeto implementa uma aplicação web simples para classificação de emails como **Produtivo** ou **Improdutivo**. O objetivo é demonstrar a construção de uma solução backend organizada, extensível e preparada para evoluir para o uso de Inteligência Artificial.

Atualmente, a classificação é realizada por meio de **regras pré-definidas**, mas a arquitetura foi desenhada para permitir a substituição ou complementação por um classificador baseado em IA sem impacto na API ou na interface.

---

## Funcionalidades

* Envio de texto de email via formulário web
* Classificação automática do conteúdo
* Classificador central com estratégia comutável (Regras / IA)
* Logging das decisões de classificação
* Estrutura preparada para upload e análise de arquivos (TXT/PDF) em evoluções futuras

---

## Arquitetura e Decisões Técnicas

### Backend

* **FastAPI** para construção da API e gerenciamento das rotas
* **Jinja2** para renderização do formulário HTML

### Classificação

* Implementação de um **classificador central**, responsável por decidir qual estratégia será utilizada
* Estratégias atuais:

  * Classificação baseada em regras
  * Placeholder para classificação baseada em IA

Essa abordagem segue princípios de **Clean Architecture** e **Open/Closed Principle**, permitindo evolução do sistema sem refatorações invasivas.

### Logging

* Logging informativo implementado no ponto central de decisão
* Registro da estratégia utilizada, resultado da classificação e prévia do texto analisado
* Facilita rastreabilidade, debug e auditoria

---

## Como Executar o Projeto

1. Clone o repositório
2. Crie e ative um ambiente virtual
3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Execute a aplicação:

```bash
uvicorn app.main:app --reload
```

5. Acesse no navegador:

```
http://127.0.0.1:8000
```

---

## Roadmap

* [x] Classificação por regras
* [x] Arquitetura preparada para IA
* [x] Logging de decisões
* [ ] Upload e parsing de arquivos TXT/PDF
* [ ] Classificação utilizando modelo de Machine Learning

---

## Observações Finais

Este projeto foi desenvolvido com foco em clareza arquitetural, boas práticas e facilidade de evolução, priorizando decisões técnicas consistentes em detrimento de complexidade desnecessária.
