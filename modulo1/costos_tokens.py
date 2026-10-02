import sys

TOKENS_PER_MILLION = 1_000_000 
DAYS_PER_MONTH = 30

MODELS = {             
            "quick": {"input": 0.25, "output": 1.25},
            "medium": {"input": 3.00, "output": 15.00},
            "max": {"input": 15.00, "output": 75.00},
                }


def calculate_cost(model, input_token, output_token):
    if model not in MODELS:
        raise ValueError(f"Model does not exist. Available: {', '.join(MODELS)}")
    if input_token < 0 or output_token < 0:
        raise ValueError("Token counts must not be negative")
    input_price = MODELS[model]["input"]
    output_price = MODELS[model]["output"]
    input_cost = input_token / TOKENS_PER_MILLION * input_price
    output_cost = output_token / TOKENS_PER_MILLION * output_price
    total = input_cost + output_cost
    return total     


def main():
    model = input("Model (quick/medium/max): ").strip().lower()
    if model not in MODELS:
        sys.exit(f"Error: Model does not exist. Available: {', '.join(MODELS)}")
    try:
        input_token = int(input("Input tokens per request: "))
        output_token = int(input("Output tokens per request: "))
        daily_request = int(input("Requests per day: "))
    except ValueError:
        sys.exit("Error: The data must be integers")
    if input_token < 0 or output_token < 0 or daily_request < 0:
        sys.exit("Error: The data must not be negative")
    request_cost = calculate_cost(model, input_token, output_token)
    daily_cost = request_cost * daily_request
    monthly_cost = daily_cost * DAYS_PER_MONTH
    print(f"Cost per request: ${request_cost:.4f}")
    print(f"Daily cost: ${daily_cost:.4f}")
    print(f"Monthly cost: ${monthly_cost:.4f}")


if __name__ == "__main__":
    main()
