def calculate_total_sales(sales_list):
    summ = 0
    for dict_ in sales_list:
        quantity = dict_.get('quantity')
        price_per_unit = dict_.get('price_per_unit')
        summ += quantity * price_per_unit
    return summ

sales_data = [
    {"product": "Футболка", "quantity": 10, "price_per_unit": 500},
    {"product": "Джинсы", "quantity": 5, "price_per_unit": 1000},
    {"product": "Кроссовки", "quantity": 3, "price_per_unit": 1500},
]

total_sales = calculate_total_sales(sales_data)
print(f"Общая стоимость проданных товаров: {total_sales}")
