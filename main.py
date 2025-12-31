import os
from dotenv import load_dotenv
from src.logger import logger
from src.bot import BinanceBot
from src.helpers import print_menu, get_user_input

load_dotenv()

def main():
    print("\n Welcome to Binance Futures Trading bot")
    print("="*60)

    API_KEY = os.getenv("API_KEY")
    SECRET_KEY = os.getenv("SECRET_KEY")

    if not API_KEY or not SECRET_KEY:
        print("API credentials are required. Please add them in your .env file.")
        return
    
    try:
        bot = BinanceBot(API_KEY, SECRET_KEY, testnet=True)
        print("BinanceBot has been initialized.")

        while True:
            print_menu()
            choice = get_user_input("Select an option: (1-8): ")

            if choice == '1':
                print("\n--- MARKET ORDER ---")
                symbol = get_user_input("Enter symbol: ").upper()
                side = get_user_input("Enter side (BUY/SELL): ").upper()
                quantity = get_user_input("Enter quantity: ", float)
                
                if quantity:
                    result = bot.place_market_order(symbol, side, quantity)
                    if result:
                        print(f"\nOrder executed successfully!")
                        print(f"Order ID: {result['orderId']}")
                        print(f"Status: {result['status']}")
            
            elif choice == '2':
                print("\n--- LIMIT ORDER ---")
                symbol = get_user_input("Enter symbol: ").upper()
                side = get_user_input("Enter side (BUY/SELL): ").upper()
                quantity = get_user_input("Enter quantity: ", float)
                price = get_user_input("Enter limit price: ", float)
                
                if quantity and price:
                    result = bot.place_limit_order(symbol, side, quantity, price)
                    if result:
                        print(f"\nOrder placed successfully!")
                        print(f"Order ID: {result['orderId']}")
            
            elif choice == '3':
                print("\n--- STOP-LIMIT ORDER ---")
                symbol = get_user_input("Enter symbol: ").upper()
                side = get_user_input("Enter side (BUY/SELL): ").upper()
                quantity = get_user_input("Enter quantity: ", float)
                stop_price = get_user_input("Enter stop price: ", float)
                limit_price = get_user_input("Enter limit price: ", float)
                
                if quantity and stop_price and limit_price:
                    result = bot.place_stop_limit_order(symbol, side, quantity, stop_price, limit_price)
                    if result:
                        print(f"\nStop-limit order placed!")
            
            elif choice == '4':
                print("\n--- ACCOUNT BALANCE ---")
                balance = bot.get_account_balance()
                if balance:
                    print(f"Total Balance: {balance['totalWalletBalance']} USDT")
                    print(f"Available: {balance['availableBalance']} USDT")
                    print("\nAssets:")
                    for asset in balance['assets']:
                        print(f"  {asset['asset']}: {asset['balance']} (Available: {asset['available']})")
            
            elif choice == '5':
                print("\n--- OPEN ORDERS ---")
                symbol = get_user_input("Enter symbol (or press Enter for all): ").upper()
                orders = bot.get_open_orders(symbol if symbol else None)
                if orders:
                    if len(orders) == 0:
                        print("No open orders")
                    else:
                        for order in orders:
                            print(f"\nOrder ID: {order['orderId']}")
                            print(f"Symbol: {order['symbol']}")
                            print(f"Side: {order['side']}")
                            print(f"Type: {order['type']}")
                            print(f"Quantity: {order['origQty']}")
                            print(f"Price: {order['price']}")
            
            elif choice == '6':
                print("\n--- POSITIONS ---")
                positions = bot.get_position_info()
                if positions:
                    if len(positions) == 0:
                        print("No active positions")
                    else:
                        for pos in positions:
                            print(f"\nSymbol: {pos['symbol']}")
                            print(f"Position Amount: {pos['positionAmt']}")
                            print(f"Entry Price: {pos['entryPrice']}")
                            print(f"Unrealized PnL: {pos['unRealizedProfit']}")
            
            elif choice == '7':
                print("\n--- CANCEL ORDER ---")
                symbol = get_user_input("Enter symbol: ").upper()
                order_id = get_user_input("Enter order ID: ", int)
                if order_id:
                    result = bot.cancel_order(symbol, order_id)
                    if result:
                        print("Order cancelled successfully")
            
            elif choice == '8':
                print("\nThank you for using the trading bot!")
                logger.info("Bot session ended by user")
                break
            
            else:
                print("Invalid option. Please select 1-8")
            
            input("\nPress Enter to continue...")
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        print(f"An Error occured in the main program: {str(e)}")



if __name__ == "__main__":
    main()