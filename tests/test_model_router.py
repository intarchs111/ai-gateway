from src.routing.model_router import route_model
from src.config.settings import Settings


def test_model_routing_in_prod_uses_configured_model():
    settings = Settings(
        openai_api_key="key",
        default_model="prod-model",
        environment="prod"
    )

    model = route_model(settings)

    assert model == "prod-model"


def test_model_routing_in_non_prod_uses_safe_default():
    settings = Settings(
        openai_api_key="key",
        default_model="prod-model",
        environment="dev"
    )

    model = route_model(settings)

    assert model == "gpt-5-nano"
