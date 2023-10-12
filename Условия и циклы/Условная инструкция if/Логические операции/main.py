# Предположим, что есть следующие условия
is_logged_in = True  # Пользователь вошел в систему
has_items_in_cart = True  # В корзине есть товары
has_shipping_address = False  # У пользователя отсутствует адрес доставки

# Проверяем, выполняются ли все необходимые условия для оформления заказа
has_order = False  # Считаем, что заказ не оформлен
if is_logged_in and has_items_in_cart and has_shipping_address:
    print("Все критерии для оформления заказа выполнены. Заказ может быть оформлен.")
    has_order = True
else:
    print("Не все критерии для оформления заказа выполнены. Пожалуйста, проверьте информацию.")

# Условия для получения скидки
min_purchase = 1000  # Минимальная стоимость для применения скидки
total_purchase = 1200  # Общая стоимость покупки
is_first_order = False  # Пользователь делает первый заказ

if has_order and (total_purchase > min_purchase or is_first_order):
    print("Вы получаете скидку!")
