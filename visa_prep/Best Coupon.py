bill_amount = int(input())
discount_percentage = bill_amount * 0.10
flat_discount = 100
max_discount = max(discount_percentage, flat_discount)
final_amount = bill_amount - max_discount
print(int(final_amount))
