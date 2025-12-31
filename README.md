# Binance Futures Testnet Trading Bot
A basic implementation of a Binance-based trading bot that focuses on Futures Testnet.

<img width="694" height="329" alt="image" src="https://github.com/user-attachments/assets/f77cf87e-e6a9-46c9-9963-fef27cd84ebb" />

## Features
### Core Features
- Market order - BUY/SELL
- Limit order execution with `time-in-force`
- Command Line Interface
- Input validations
- Detailed logger
- API Exception handling
- Account & Order status
- Order cancellation

## Prerequisites

- Python 3.7
- Binance Futures Testnet account
- API Key and Secret keys generated from Binance Futures Testnet 

## Setup 
### 1. Register on Binance Testnet

1. Visit [Binance Futures Testnet](https://testnet.binancefuture.com)
2. Register for a testnet account
3. Navigate to Demo Trading API
4. Generate API credentials from API Management from the Account section
5. Save your `API_KEY` and `SECRET_KEY` securely under `.env` file

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

## Usage
### Starting the Bot

1. Run the script:
2. 
   ```bash
   python trading_bot.py
   ```
   
3. Use the interactive menu to perform operations

### Menu Options

1. **Place Market Order** - Execute immediate buy/sell at current market price
2. **Place Limit Order** - Set a specific price for order execution
3. **Place Stop-Limit Order** - Advanced order with stop trigger and limit price
4. **View Account Balance** - Check your USDT balance and asset allocation
5. **View Open Orders** - List all pending orders
6. **View Positions** - Check your current futures positions
7. **Cancel Order** - Cancel a specific order by ID
8. **Exit** - Close the application

### Example Usage

#### Placing a Market Order
```
Select option: 1
Enter symbol: BTCUSDT
Enter side: BUY
Enter quantity: 0.001
```

#### Placing a Limit Order
```
Select option: 2
Enter symbol: ETHUSDT
Enter side: SELL
Enter quantity: 0.1
Enter limit price: 3500
```

#### Placing a Stop-Limit Order
```
Select option: 3
Enter symbol: BTCUSDT
Enter side: SELL
Enter quantity: 0.001
Enter stop price: 95000
Enter limit price: 94500
```

## Logging

This bot generates logs with timestamps:

- **File Logging**: `trading_bot_YYYYMMDD_HHMMSS.log`
- **Console Logging**: Real-time output to terminal
  

## Code Structure

```
trading_bot.py
├── BasicBot (Main Class)
│   ├── __init__()              # Initialize client and test connection
│   ├── _validate_symbol()      # Validate trading pairs
│   ├── _log_request()          # Log API requests
│   ├── _log_response()         # Log API responses
│   ├── place_market_order()    # Places market orders
│   ├── place_limit_order()     # Places limit orders
│   ├── place_stop_limit_order() # Places stop-limit orders
│   ├── get_account_balance()   # Gets account info
│   ├── get_open_orders()       # Lists open orders
│   ├── get_position_info()     # Lists positions
│   └── cancel_order()          # Cancel orders
├── print_menu()                # Display CLI menu
├── get_user_input()            # Handle user input 
└── main()                      # Main loop
```

## Error Handling

The bot implements error handling:

- **BinanceAPIException**: Handles API-specific errors (invalid symbols, insufficient balance)
- **BinanceRequestException**: Handles network and request errors
- **Input Validation**: Validates all user inputs before API calls
- **Symbol Validation**: Verifies trading pair existence
- **Quantity Validation**: Ensures positive order quantities
- **Price Validation**: Checks price values are valid

## Binance API Documentation

- [Binance Futures API Documentation](https://binance-docs.github.io/apidocs/futures/en/)
- [python-binance Library](https://python-binance.readthedocs.io/)
