from app.llm import generate_response

def run_agent(user_input: str) -> dict:
    resposta = generate_response(user_input)

    return {
        "input": user_input,
        "output": resposta,
        "status": "success"
    }
