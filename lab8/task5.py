def convert_date_format(date_str):
    """Convert date from 'YYYY-MM-DD' to 'DD-MM-YYYY' format."""
    parts = date_str.strip().split('-')
    if len(parts) != 3:
        raise ValueError("Input date must be in 'YYYY-MM-DD' format")
    yyyy, mm, dd = parts
    return f"{dd}-{mm}-{yyyy}"

if __name__ == "__main__":
    date_input = input("Enter date in YYYY-MM-DD format: ")
    try:
        converted = convert_date_format(date_input)
        print("Converted date:", converted)
    except Exception as e:
        print("Error:", e)
