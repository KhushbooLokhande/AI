from datetime import datetime

def greet_user():
    current_time = datetime.now()
    hour = current_time.hour
    if hour < 12:
        return "Good morning! Welcome to ShopEase, your online shopping assistant!"
    elif 12 <= hour < 16:
        return "Good afternoon! Welcome to ShopEase, your online shopping assistant!"
    else:
        return "Good evening! Welcome to ShopEase, your online shopping assistant!"

def show_menu():
    print("\nWelcome to ShopEase! Please choose an option:")
    options = {
        "1": "Browse Products",
        "2": "View Cart",
        "3": "Place Order",
        "4": "Track Order",
        "5": "Customer Support",
        "6": "Exit"
    }
    
    for key, value in options.items():
        print(f"{key}. {value}")

def handle_browse_products():
    print("\nProduct Categories:")
    print("1. Electronics")
    print("2. Fashion")
    print("3. Home Appliances")
    print("4. Books")
    print("5. Beauty Products")
    category = input("Enter the number of the category you'd like to browse: ")
    print(f"Fetching products for category {category}...")
    
    if category == "1":
        print("Available Electronics:")
        print("1. Laptop - $999")
        print("2. Smartphone - $699")
        print("3. Headphones - $199")
    elif category == "2":
        print("Available Fashion Items:")
        print("1. T-Shirt - $25")
        print("2. Sneakers - $79")
        print("3. Jacket - $120")
    elif category == "3":
        print("Available Home Appliances:")
        print("1. Air Fryer - $89")
        print("2. Vacuum Cleaner - $199")
        print("3. Microwave Oven - $299")
    elif category == "4":
        print("Available Books:")
        print("1. Fiction Novel - $15")
        print("2. Science Book - $35")
        print("3. History Book - $20")
    elif category == "5":
        print("Available Beauty Products:")
        print("1. Moisturizer - $18")
        print("2. Lipstick - $12")
        print("3. Perfume - $45")
    else:
        print("Invalid category selection.")

def handle_view_cart():
    print("\nYour Cart:")
    print("- Item 1: Laptop - $999")
    print("- Item 2: Sneakers - $79")
    print("Total: $1078")

def handle_place_order():
    print("\nPlacing your order...")
    shipping_address = input("Enter your shipping address: ")
    payment_method = input("Enter your payment method (Credit Card, PayPal, etc.): ")
    print("✅ Order placed successfully! Your order will be delivered soon.")

def handle_track_order():
    order_id = input("Enter your Order ID: ")
    print(f"Tracking details for Order {order_id}: Your order is out for delivery!")

def handle_customer_support():
    print("\nCustomer Support:")
    print("1. Refund & Return Policy")
    print("2. Order Issues")
    print("3. Account Management")
    query = input("Enter your query number: ")
    print(f"Fetching support details for query {query}...")

def chatbot_menu():
    print(greet_user())
    while True:
        show_menu()
        choice = input("Enter the number of your choice: ")
        
        if choice == "1":
            handle_browse_products()
        elif choice == "2":
            handle_view_cart()
        elif choice == "3":
            handle_place_order()
        elif choice == "4":
            handle_track_order()
        elif choice == "5":
            handle_customer_support()
        elif choice == "6":
            print("Thank you for shopping with ShopEase! Have a great day!")
            break
        else:
            print("Invalid choice. Please try again.")

chatbot_menu()
