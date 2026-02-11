import logging

logging.basicConfig(level=logging.INFO)


def log_request_model(model: str) -> None:    
    logging.info("Invoking model: %s", model)

def log_gateway_request() -> None:    
    logging.info("Initializing AI_Gateway")

def log_gateway_error() -> None:    
    logging.error("AI_Gateway invocation failed\n")  

def log_prompt_build() -> None:    
    logging.info("Building prompt for AI_Gateway request")

def log_model_routing(model: str) -> None:    
    logging.info("Routing to model: %s", model)

def log_llm_usage_metrics(usage: str) -> None:    
    logging.info("LLM usage metrics: %s", usage)