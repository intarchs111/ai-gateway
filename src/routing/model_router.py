from config.settings import Settings


def route_model(settings: Settings) -> str:
    if settings.environment == "prod":
        return settings.default_model

    return "gpt-5-nano"
