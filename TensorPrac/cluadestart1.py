import anthropic
import os

client = anthropic.Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY")
)

client = anthropic.Anthropic(api_key="your_actual_api_key_here")
message = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=2000,
    temperature=0,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Tell me 10 short puns about computers."
                }
            ]
        }
    ]
)
print(message.content)