product_code = int(input("Enter the product code (1 for Battery Based Toys, 2 for Key-based Toys, 3 for Electrical Charging Based Toys): "))
order_amount = float(input("Enter the order amount in Rs: "))
net_amount = order_amount
if product_code == 1:  
    if order_amount > 1000:
        discount = 0.10 
        net_amount = order_amount - (order_amount * discount)
elif product_code == 2: 
    if order_amount > 100:
        discount = 0.05 
        net_amount = order_amount - (order_amount * discount)

elif product_code == 3: 
    if order_amount > 500:
        discount = 0.10 
        net_amount = order_amount - (order_amount * discount)
print(f"The net amount to be paid after discount is: Rs {net_amount:.2f}")
