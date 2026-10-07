import sys

TOKENS_PER_MILLION = 1_000_000 
DAYS_PER_MONTH = 30

MODELS = {             
            "quick": {"input": 0.25, "output": 1.25},
            "medium": {"input": 3.00, "output": 15.00},
            "max": {"input": 15.00, "output": 75.00},
                }


def validate_model(model):
     if model not in MODELS:
        raise ValueError(f"Model does not exist. Available: {', '.join(MODELS)}")

def calculate_cost(model, input_tokens, output_tokens):
    validate_model(model)
    if input_tokens < 0 or output_tokens < 0:
        raise ValueError("Token counts must not be negative")
    input_price = MODELS[model]["input"]
    output_price = MODELS[model]["output"]
    input_cost = input_tokens / TOKENS_PER_MILLION * input_price
    output_cost = output_tokens / TOKENS_PER_MILLION * output_price
    total = input_cost + output_cost
    return total     


def main():
    model = input("Model (quick/medium/max): ").strip().lower()
    try:
        validate_model(model)
    except ValueError as error:
        sys.exit(f"Error: {error}")
    try:
        input_tokens = int(input("Input tokens per request: "))
        output_tokens = int(input("Output tokens per request: "))
        daily_requests = int(input("Requests per day: "))
    except ValueError:
        sys.exit("Error: The data must be integers")
    if daily_requests < 0:
        sys.exit("Error: Requests per day must not be negative")
    try:
        request_cost = calculate_cost(model, input_tokens, output_tokens)
    except ValueError as error:
        sys.exit(f"Error: {error}")
    daily_cost = request_cost * daily_requests
    monthly_cost = daily_cost * DAYS_PER_MONTH
    print(f"Cost per request: ${request_cost:.4f}")
    print(f"Daily cost: ${daily_cost:.4f}")
    print(f"Monthly cost: ${monthly_cost:.4f}")


if __name__ == "__main__":
    main()
