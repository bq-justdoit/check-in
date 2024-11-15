api_key = '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'



from openai import OpenAI

client = OpenAI(api_key=api_key)


completion = client.chat.completions.create(
    model="gpt-4o-mini-2024-07-18",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello!"}
    ]
)

print(completion.choices[0].message)

exit()
stream = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Say this is a test"}],
    stream=True,
)
for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")