"""
AI Gateway v1.0.0 — Failure Path Example

Use case:
- Demonstrate how failures are handled at the gateway boundary
- Applications receive structured, provider-agnostic errors
"""

from ai_gateway import AIGateway
from config import Settings
from ai_gateway import GatewayInvocationError


def main() -> None:

    print("\n--- AI Gateway Request ---\n")

    # Define invalid input to trigger a controlled failure
    USER_INPUT = ""

    # Initialize the AI Gateway (single integration point)
    gateway = AIGateway(settings=Settings())

    print("\n--- AI Gateway Response ---\n")
    
    # Invoke the gateway with a user input that triggers an error
    try:
        response_text = gateway.invoke(
            user_input=USER_INPUT
        )
        print(response_text)
    except GatewayInvocationError as err:        
        print(f"Error type   : {err.error_type}")
        print(f"Error message: {err.message}")

    print("\n---------------------------\n")
    
if __name__ == "__main__":
    main()
