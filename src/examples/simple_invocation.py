"""
AI Gateway v1.0.0 — Minimal Invocation Example

Use case:
- Demonstrate LLM access via a centralized platform boundary
- No application code calls OpenAI directly
"""

from ai_gateway import AIGateway
from ai_gateway.errors import GatewayInvocationError
from config import Settings


def main() -> None:    

    print("\n--- AI Gateway Request ---\n")

    # Define a simple user input for OpenAI invocation
    USER_INPUT = "Explain the purpose of AI in enterprise systems in one line sentence."       

    try:
        # Initialize the AI Gateway (single integration point) with settings (model, apikey, env)
        gateway = AIGateway(settings=Settings())
        
        # Invoke the gateway with a user input 
        response_text = gateway.invoke(
            user_input=USER_INPUT
        )
        print("\n--- AI Gateway Response ---\n")
        # Output response content only (application-facing contract)  
        print(response_text)
    except GatewayInvocationError as err:   
        # print error details in case of failure
        print("\n--- AI Gateway Response ---\n")     
        print(f"Error type   : {err.error_type}")
        print(f"Error message: {err.message}")    
    
    print("\n---------------------------\n")


if __name__ == "__main__":
    main()