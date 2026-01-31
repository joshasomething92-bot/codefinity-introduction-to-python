def apply_discount(price, discount=0.05):
    return price * (1 - discount)
    

def apply_tax(price, tax=0.07):
    return price * (1 + tax)
    

def calculate_total(price, discount=0.05, tax=0.07):
    discounted_price = apply_discount(price, discount)
    final_total = apply_tax(discounted_price, tax)
    return final_total

default_discount = calculate_total(120, discount=0.05, tax=0.07)
print(f"Total cost with default discount and tax: ${default_discount}")
custom_discount = calculate_total(100, discount=0.10, tax=0.08)
print(f"Total cost with custom discount and tax: ${custom_discount:.2f}")

    
    
    