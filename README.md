# 🍔 Smart Menu Recommender API

Microsserviço de back-end em Python construído com **FastAPI** e integrado a **LLMs** para recomendação contextualizada de pratos de delivery. Desenvolvido como projeto de portfólio para o processo seletivo do **Programa de Estágio GenAI do iFood (2027)**.

---

## 🚀 Sobre o Projeto
Este projeto simula um componente do ecossistema de inteligência artificial voltado para a experiência do cliente no iFood. A API recebe requisições contendo o perfil de fome, restrições alimentares e preferência culinária do usuário, cruza esses dados com um cardápio dinâmico e utiliza inteligência artificial para gerar recomendações personalizadas.

Além disso, o sistema conta com um **mecanismo de fallback resiliente**, garantindo alta disponibilidade e respostas instantâneas mesmo em caso de latência ou instabilidade temporária na API de IA.

---

## 🛠️ Tecnologias Utilizadas
* **Python**
* **FastAPI** (Framework web de alta performance)
* **Pydantic** (Validação de dados e tipagem)[cite: 1]
* **Google GenAI SDK** (Integração com LLMs)
* **Uvicorn** (Servidor ASGI)

---

## ⚙️ Como Executar o Projeto Localmente

Para colocar a aplicação para rodar no seu computador de forma sequencial, execute os comandos abaixo no seu terminal:

```bash
# 1. Clone o repositório
git clone [https://github.com/SEU_USUARIO/ifood-smart-menu-api.git](https://github.com/SEU_USUARIO/ifood-smart-menu-api.git)
cd ifood-smart-menu-api

# 2. Crie e ative um ambiente virtual
python -m venv venv
# No Windows (PowerShell): .\venv\Scripts\Activate
# No Linux/Mac: source venv/bin/activate

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Configure sua chave de API do Gemini (Substitua pela sua chave)
# No Linux/Mac/Git Bash:
export GEMINI_API_KEY="sua_chave_aqui"
# No Windows PowerShell:
$env:GEMINI_API_KEY="sua_chave_aqui"

# 5. Inicie o servidor da API
uvicorn main:app --reload
```
---

## 🤖 Notas de Desenvolvimento

Este projeto foi desenvolvido de forma colaborativa com o auxílio do Google Gemini (modelo Gemini 2.5 Flash / 3.8 Flash via SDK oficial google-genai), utilizado como assistente de planejamento técnico, estruturação de código e refatoração arquitetural.
