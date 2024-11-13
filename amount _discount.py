product_code = int(input("Enter toy code (1-Battery, 2-Key, 3-Electrical): "))
order_amount = float(input("Enter the order amount (Rs): "))
if product_code == 1 and order_amount > 1000:
    order_amount *= 0.90  #Net Amount=Original Amount×(1−Discount Rate)
elif product_code == 2 and order_amount > 100:
    order_amount *= 0.95  
elif product_code == 3 and order_amount > 500:
    order_amount *= 0.90 
print("Total amount after discount: Rs.", order_amount)

