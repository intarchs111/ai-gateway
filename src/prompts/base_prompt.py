from prompts.templates import SYSTEM_TEMPLATE


def build_prompt(user_input: str, context: dict | None = None) -> list[dict]:
    input_blocks = [
        {
            "role": "system",
            "content": SYSTEM_TEMPLATE
        }
    ]

    if context:
        input_blocks.append({
            "role": "system",
            "content": f"Context: {context}"
        })

    input_blocks.append({
        "role": "user",
        "content": user_input
    })

    return input_blocks
