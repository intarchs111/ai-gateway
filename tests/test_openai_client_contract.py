from unittest.mock import MagicMock
from src.clients.openai_client import OpenAIClient
from src.config.settings import Settings


def test_openai_client_returns_text_and_usage(monkeypatch):
    settings = Settings(openai_api_key="key")
    client = OpenAIClient(settings)

    mock_response = MagicMock()
    mock_response.output_text = "hello"
    mock_response.usage = {"total_tokens": 5}

    mock_client = MagicMock()
    mock_client.responses.create.return_value = mock_response

    client.client = mock_client

    text, usage = client.invoke(
        model="test-model",
        input_data=[{"role": "user", "content": "hi"}]
    )

    assert text == "hello"
    assert usage["total_tokens"] == 5
