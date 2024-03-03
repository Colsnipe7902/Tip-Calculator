 
welcome_banner = """Welcome to Tip Calculater"""
print(welcome_banner)
order_total = float(input("How much did you pay?"))
tip_percent = float(input("How much percent do you want to tip?"))
order_total_with_tip = order_total * tip_percent
tip_money = order_total_with_tip + order_total
print(f"Your tip amount is {order_total_with_tip}")
print(f"The total amount that you have to pay with the tip is {tip_money}  ")
