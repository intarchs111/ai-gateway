from unittest.mock import MagicMock
from src.ai_gateway.gateway import AIGateway
from src.config import Settings


def test_gateway_invokes_components_in_order(monkeypatch):
    settings = Settings(openai_api_key="test-key")
    gateway = AIGateway(settings)

    monkeypatch.setattr(
        "ai_gateway.gateway.build_prompt",
        lambda user_input, context: [{"role": "user", "content": user_input}]
    )

    monkeypatch.setattr(
        "ai_gateway.gateway.route_model",
        lambda settings: "test-model"
    )

    mock_client = MagicMock()
    mock_client.invoke.return_value = ("response", {"total_tokens": 10})
    gateway.client = mock_client

    response = gateway.invoke("hello")

    assert response == "response"
    mock_client.invoke.assert_called_once()
