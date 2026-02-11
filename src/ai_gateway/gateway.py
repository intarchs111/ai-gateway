from config.settings import Settings
from prompts.base_prompt import build_prompt
from routing.model_router import route_model
from clients.openai_client import OpenAIClient
import observability.logger as logger
from observability.metrics import record_metrics
from ai_gateway.errors import GatewayInvocationError

class AIGateway:
    def __init__(self, settings: Settings):
        logger.log_gateway_request()
        self.settings = settings
        try:
            self.client = OpenAIClient(settings)
        except RuntimeError as e:
            logger.log_gateway_error()
            raise GatewayInvocationError(
                error_type="CONFIGURATION_ERROR",
                message=str(e)
            )
        

    def invoke(self, user_input: str, context: dict | None = None) -> str:    

        if user_input is None or not user_input.strip():
            logger.log_gateway_error()   
                     
            raise GatewayInvocationError(
                error_type="VALIDATION_ERROR",
                message="Request input must not be empty"                
            )
        
        logger.log_prompt_build()
        prompt_input = build_prompt(user_input, context)
       
        model = route_model(self.settings)
        logger.log_model_routing(model=model)
        
        try:
            logger.log_request_model(model=model)
            response_text, usage = self.client.invoke(
            model=model,
            input_data=prompt_input
        )
        except RuntimeError as e:
            logger.log_gateway_error()
            raise GatewayInvocationError(
                error_type="PROVIDER_ERROR",
                message=str(e)
            )
        except Exception as exc:
            logger.log_gateway_error()  
            raise GatewayInvocationError(
                error_type="PROVIDER_ERROR",
                message="LLM provider invocation failed"                
            ) 
               
        record_metrics(usage)

        return response_text
