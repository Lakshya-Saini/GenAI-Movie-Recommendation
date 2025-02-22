from openai import OpenAI
client = OpenAI()

def call_openai(user_prompt, system_prompt, model, temperature=0, max_tokens=2000):
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "user", "content": [{"type": "text", "text": user_prompt}]},
                {"role": "system", "content": [{"type": "text", "text": system_prompt}]}
            ],
            temperature=temperature,
            max_tokens=max_tokens
        )
        return response.choices[0].message.content
    
    except Exception as e:
        return f"Error: {str(e)}"
