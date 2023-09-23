def calculate_discounted_price(item1_price, item2_price, item3_price, item_combo):
    # Calculate the total price for individual items
    total_price = 0

    if 'item1' in item_combo:
        total_price += item1_price
    if 'item2' in item_combo:
        total_price += item2_price
    if 'item3' in item_combo:
        total_price += item3_price

    # Apply discounts based on the selected items
    if len(item_combo) == 1:
        # No discount for individual items
        final_price = total_price
        discount_percent = 0
    elif len(item_combo) == 2:
        # 10% discount for a combo pack with two unique items
        final_price = total_price * 0.9
        discount_percent = 10
    else:
        # 25% discount for the gift pack containing all three items
        final_price = total_price * 0.75
        discount_percent = 25

    return final_price, discount_percent
