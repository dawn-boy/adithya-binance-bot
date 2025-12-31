def print_menu():
    print("\n" + "="*60)
    print("BinanceBot MainMenu | by Adithya")
    print("="*60)
    print("1. Place Market Order")
    print("2. Place Limit Order")
    print("3. Place Stop-Limit Order")
    print("4. View Account Balance")
    print("5. View Open Orders")
    print("6. View Positions")
    print("7. Cancel Order")
    print("8. Exit")
    print("="*60)

def get_user_input(prompt: str, input_type: type=str):
    while True:
        try: 
            value = input(prompt)
            if input_type == float:
                return float(value)
            elif input_type == int:
                return int(value)
            else:
                return value
        except ValueError:
            print(f"Invalid input.")