products = {
    "laptop": 850000,
    "mobile": 300000,
    "keyboard": 18000,
    "mouse": 10000,
    "headphones": 12000
}

while True:

    print("\n===== INVENTORY SYSTEM =====")
    print("1. Display Products")
    print("2. Search Product")
    print("3. Sort Products by Price")
    print("4. Add Product")
    print("5. Update Product Price")
    print("6. Delete Product")
    print("7. Exit")

    choice = int(input("Enter your choice: "))


    if choice == 1:

        for name, price in products.items():
            print("Product:", name, "| Price: ₹", price)


    elif choice == 2:

        name = input("Enter product name: ")

        if name in products:
            print("Product:", name)
            print("Price: ₹", products[name])
        else:
            print("Product not found!")


    elif choice == 3:

        sorted_products = sorted(
            products.items(),
            key=lambda x: x[1]
        )

        for name, price in sorted_products:
            print("Product:", name, "| Price: ₹", price)


    elif choice == 4:

        name = input("Enter product name: ")
        price = float(input("Enter price: "))

        products[name] = price

        print("Product added successfully!")


    elif choice == 5:

        name = input("Enter product name: ")

        if name in products:
            price = float(input("Enter new price: "))
            products[name] = price

            print("Price updated successfully!")
        else:
            print("Product not found!")


    elif choice == 6:

        name = input("Enter product name: ")

        if name in products:
            del products[name]

            print("Product deleted successfully!")
        else:
            print("Product not found!")

 
    elif choice == 7:

        print("Thank you!")
        break

    else:
        print("Invalid choice!")
