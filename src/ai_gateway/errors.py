class GatewayInvocationError(Exception):
    """
    Gateway-defined exception.

    Ensures applications never depend on provider-specific errors.
    """

    def __init__(self, error_type: str, message: str):
        self.error_type = error_type
        self.message = message
        super().__init__(f"{error_type}: {message}")
