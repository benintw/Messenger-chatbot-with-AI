import openai

from .config import Config

client = openai.OpenAI(api_key=Config.OPENAI_API_KEY)


def get_ai_response(prompt: str) -> str:
    system_prompt = (
        "You are a friendly, bilingual (Chinese and English) fitness center assistant for Fitopia. "
        "Always answer questions about gym services, membership, and fitness in a helpful, concise, and polite way. "
        "If you don't know the answer, say so honestly. 如果對方用中文問我，請用中文回答!!"
        "簡短回應就好，不要回一堆字，操你媽"
    )
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
        ],
        max_tokens=256,
        temperature=0.7,
    )
    return response.choices[0].message.content.strip()
