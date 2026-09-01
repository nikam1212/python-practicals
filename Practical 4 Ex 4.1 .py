status = input("Enter order status: ").lower()

if status == "pending":
    print("Your order is pending and will be processed soon.")

elif status == "shipped":
    print("Your order has been shipped and is on the way.")

elif status == "delivered":
    print("Your order has been delivered successfully.")

elif status == "processing":
    print("Your order is currently being processed.")

else:
    print("Invalid order status.")
 