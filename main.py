import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional
from google import genai

# Inicializa a aplicação FastAPI
app = FastAPI(
    title="iFood Smart Menu Recommender API",
    description="API de recomendação de pratos contextualizados usando IA para o processo seletivo do iFood.",
    version="1.0.0"
)

# Configuração do cliente Gemini
try:
    client = genai.Client()
except Exception as e:
    client = None

# Modelo de dados de entrada usando Pydantic
class ClientePreferencias(BaseModel):
    fome: str  # Ex: "leve", "moderada", "grande"
    restricoes: Optional[List[str]] = Field(default_factory=list)  # Ex: ["vegetariano", "sem lactose"]
    preferencia_culinaria: str  # Ex: "italiana", "brasileira", "japonesa"

# Rota raiz para verificar se a API está no ar
@app.get("/")
def ler_raiz():
    return {"mensagem": "Bem-vindo à API de Recomendação do iFood GenAI! O sistema está online."}

# Rota principal de recomendação integrada com IA e Fallback
@app.post("/recomendar")
def recomendar_prato(preferencias: ClientePreferencias):
    # Cardápio fictício do iFood para servir de contexto para a IA
    cardapio_ifood = """
    1. Bowl Saudável de Quinoa com Frango Grelhado (Sem glúten, leve)
    2. Pizza Margherita Artesanal com Massa Fermentada 48h (Vegetariana, moderada)
    3. Feijoada Completa Tradicional com Arroz, Couve e Farofa (Grande, pesada)
    4. Poke Hawaiano de Salmão Fresco com Manga e Abacate (Leve, sem lactose)
    5. Burger Artesanal Angus com Queijo Cheddar e Bacon (Grande)
    """

    # Montando o prompt estruturado
    prompt = f"""
    Você é um assistente de recomendação de restaurantes do iFood.
    Com base no seguinte cardápio:
    {cardapio_ifood}

    Recomende o melhor prato para um cliente com as seguintes características:
    - Nível de fome: {preferencias.fome}
    - Restrições alimentares: {', '.join(preferencias.restricoes) if preferencias.restricoes else 'Nenhuma'}
    - Preferência culinária: {preferencias.preferencia_culinaria}

    Retorne o nome do prato escolhido do cardápio e uma breve justificativa de por que ele é ideal para o cliente.
    """

    recomendacao_final = ""
    origem_resposta = "ia"

    try:
        if not client:
            raise Exception("Cliente Gemini não inicializado.")
            
        # Chamada ao modelo Gemini
        response = client.models.generate_content(
            model='gemini-3.8-flash',
            contents=prompt,
        )
        recomendacao_final = response.text
        
    except Exception as e:
        # PLANO B (Fallback): Se a IA falhar ou estiver com alta demanda, o sistema assume uma resposta padrão
        origem_resposta = "fallback_sistema"
        recomendacao_final = (
            f"[Modo de Contingência] Com base na sua preferência ({preferencias.preferencia_culinaria}) "
            f"e nível de fome ({preferencias.fome}), recomendamos a Pizza Margherita Artesanal "
            f"ou o Bowl Saudável, garantindo agilidade no atendimento do iFood!"
        )

    return {
        "status": "sucesso",
        "origem": origem_resposta,
        "preferencias_enviadas": preferencias,
        "recomendacao": recomendacao_final
    }