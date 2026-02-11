import os
from dataclasses import dataclass
from dotenv import load_dotenv

# Load environment variables once at module import
load_dotenv()

@dataclass(frozen=True)
class Settings:    
    openai_api_key: str = os.getenv("OPENAI_API_KEY", "")
    default_model: str = os.getenv("OPENAI_DEFAULT_MODEL", "gpt-5-nano")
    environment: str = os.getenv("ENVIRONMENT", "dev")
