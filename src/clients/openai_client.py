from xml.parsers.expat import model
from openai import OpenAI, AuthenticationError
from config import settings
from config.settings import Settings


class OpenAIClient:
    def __init__(self, settings: Settings):
        api_key=settings.openai_api_key
        if not api_key:
            raise RuntimeError("OPENAI_API_KEY is not set in environment.")
        else:            
            self.client = OpenAI(api_key=api_key)        

    def invoke(
        self,
        model: str,
        input_data: list[dict]
    ) -> tuple[str, dict | None]:
        
        try:
            output_text = None
            usage = None

            response = self.client.responses.create(
                model=model,
                input=input_data
            )
            output_text = response.output_text
            usage = response.usage
        except AuthenticationError as e:
            # Handle the specific authentication error            
            error_json = e.response.json()
            output_text = error_json['error']['message']
            raise RuntimeError(f"OPENAI Authentication Error: {output_text}")                 
            
        except Exception as e:
            # Handle other potential errors (e.g., APIConnectionError, RateLimitError)           
            error_json = e.response.json()
            output_text = error_json['error']['message']
            error_message = f"An unexpected error occurred: {output_text}"
            exception = Exception(str(error_message))
            raise exception     
        

        return output_text, usage
