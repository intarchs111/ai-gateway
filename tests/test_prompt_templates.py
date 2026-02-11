from src.prompts.base_prompt import build_prompt


def test_prompt_contains_system_and_user_roles():
    prompt = build_prompt("hello")

    roles = [block["role"] for block in prompt]

    assert roles[0] == "system"
    assert roles[-1] == "user"
