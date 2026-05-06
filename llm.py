from openai import OpenAI


client = OpenAI(
    api_key="sk-bcd5fd7f106445899f2e58c62333aa71",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)


def ask_llm(user_input: str):
    response = client.chat.completions.create(
        model="qwen3.5-flash",
        messages=[
            {"role": "system", "content": "你是一个智能助手，会判断用户是否想查询天气"},
            {"role": "user", "content": user_input}
        ]
    )

    return response.choices[0].message.content