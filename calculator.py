"""A simple command-line calculator for basic arithmetic."""


def calculate(first_number: float, operator: str, second_number: float) -> float:
    """Perform an arithmetic operation and return its result."""
    if operator == "+":
        return first_number + second_number
    if operator == "-":
        return first_number - second_number
    if operator == "*":
        return first_number * second_number
    if operator == "/":
        if second_number == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return first_number / second_number
    raise ValueError("Unsupported operator. Choose +, -, *, or /.")


def main() -> None:
    print("Simple Calculator (+, -, *, /)")
    try:
        first_number = float(input("Enter the first number: "))
        operator = input("Enter an operator (+, -, *, /): ").strip()
        second_number = float(input("Enter the second number: "))
        result = calculate(first_number, operator, second_number)
        print(f"Result: {result:g}")
    except ValueError as error:
        print(f"Input error: {error}")
    except ZeroDivisionError as error:
        print(f"Math error: {error}")


if __name__ == "__main__":
    main()
