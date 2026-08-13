customer_name=input("Enter Customer Name : ")
product_name=input("Enter Product Name : ")
feedback=input("Enter your Feedback : ")

customer_name=customer_name.strip().title()
product_name=product_name.strip().title()
feedback=feedback.capitalize().strip()

print("========== Feedback ===========")
print("Customer Name :",customer_name)
print("Product Name :",product_name)
print("Feedback :",feedback)

print("====== Thank You for your Feedback ==========")